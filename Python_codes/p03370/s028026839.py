L=list()
N,M=map(int,input().split())
for i in range(N):
  L.append(int(input()))
M-=sum(L)
ans=0
ans+=N
print(ans+(M//min(L)))