N,K=map(int,input().split())
res = K
for i in range(1,N):
  res=res*(K-1)
print(res)