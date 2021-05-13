N,M=map(int,input().split())
A=list(map(int,input().split()))
weight=[0,2,5,5,4,5,6,3,7,6]
li=[-100]*(N+1)
li[0]=0
for i in range(N+1):
  for a in A:
    if weight[a]+i<=N:
      li[weight[a]+i]=max(li[weight[a]+i],a+10*li[i])
print(li[N])