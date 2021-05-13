N,K=map(int,input().split())
DIV=10**9+7

num=[0]*(K+1)
ans=0

for x in range(K,0,-1):
  num[x]=pow(K//x,N,DIV)
  for temp in range(x*2,K+1,x):
    num[x]-=num[temp]
  ans += num[x] * x
  ans %= DIV

print(ans)