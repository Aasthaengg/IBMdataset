from collections import defaultdict, deque
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    return g1[n] * g2[r] % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N, K = map(int, input().split())
dic = defaultdict(list)
for i in range(N-1):
  a, b = map(int, input().split())
  dic[a-1] += [b-1]
  dic[b-1] += [a-1]

log = [float('inf')]*N
log[0] = 0
q = deque([0])
ans = K
while q:
  p = q.popleft()
  if log[p]<1:
    ans *= cmb(K-1,K-1-len(dic[p]),mod)
  else:
    ans *= cmb(K-2,K-1-len(dic[p]),mod)
  ans %= mod
  for e in dic[p]:
    if log[e]>log[p]+1:
      q += [e]
      log[e] = log[p]+1
print(ans)
