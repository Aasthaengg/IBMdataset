from collections import deque

def P(n, r):
    if ( r<0 or r>n ):
        return 0
    return g1[n] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5+30
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


n,k=map(int,input().split())
G=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  a=a-1
  b=b-1
  G[a].append(b)
  G[b].append(a)
D=deque([0])
DD=[0]
V=[0]*n
V[0]=1
GG=[[] for i in range(n)]
while len(D)>0:
  x=D[0]
  D.popleft()
  for i in range(len(G[x])):
    if V[G[x][i]]==0:
      V[G[x][i]]=1
      GG[x].append(G[x][i]) #子ノードのlist
      D.append(G[x][i])
      DD.append(G[x][i])
ans=k*P(k-1,len(GG[0]))%mod  #頂点0,0の子の色の付け方
for i in range(1,n):  #子の色を決めていく
  if len(GG[i])==0:
    continue
  ans=ans*P(k-2,len(GG[i]))%mod
print(ans)