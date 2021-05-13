from collections import deque
import sys
input = sys.stdin.readline
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    return g1[n] * g2[n-r]  % mod

mod = 10**9+7 #出力の制限
N = 10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N,K=map(int,input().split())
ki=[[] for f in range(N)]
for i in range(N-1):
 a,b = map(int,input().split())
 ki[a-1].append(b-1)
 ki[b-1].append(a-1)
stack = deque([0])
check = [0]*N #チェック済みリスト
c=0
t=0
ans=1
while stack != deque([]) :
 a=stack.popleft()
 check[a]=1
 if len(ki[a])+1>K:
  t=1
  break
 else:
  for i in ki[a]:
   if check[i]==0:
    stack.append(i)
  ans*=cmb(K-c,len(ki[a])+1-c,mod)
  ans%=(10**9+7)
  c=2
if t==1:
 print(0)
else:
 print(ans)