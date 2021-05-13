N=int(input())
A=[]
B=[]
for _ in range(N):
  a, b=map(int, input().split())
  tmpa=a%b
  A.append(tmpa)
  B.append(b)
ans=0
for i in range(N-1, -1, -1):
  tmp=B[i]-(A[i]+ans)%B[i]
  if tmp==B[i]:
    tmp=0
  ans+=tmp
print(ans)
  
