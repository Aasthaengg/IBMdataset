N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort(key=lambda x:x[1])
ans=0
for i in range(N):
  if ans+A[i][0]>A[i][1]:
    print('No')
    exit()
  ans+=A[i][0]
print('Yes')