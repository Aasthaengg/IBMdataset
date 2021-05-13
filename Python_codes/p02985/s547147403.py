from collections import deque
n,k=map(int,input().split())
edge=[[] for _ in range(n)]
visited=[-1]*n
def pmt(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    return g1[n]* g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
for _ in range(n-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  edge[a].append(b)
  edge[b].append(a)
stack=deque([])
visited[0]=0
for e in edge[0]:
  stack.append(e)
  visited[e]=0
def dfs():
  ans=k*pmt(k-1,len(edge[0]),mod)%mod
  while stack:
    p=stack.pop()
    cnt=0
    for c in edge[p]:
      if visited[c]==-1:
        cnt+=1
        visited[c]=0
        stack.append(c)
    ans=ans*pmt(k-2,cnt,mod)%mod
  return ans%mod
print(dfs())