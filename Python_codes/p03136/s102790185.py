N=int(input())
A=sorted(map(int,input().split()))
ans=0
for i in range(N-1):
  ans+=A[i]

if ans<=A[N-1]:
  print("No")
else:
  print("Yes")