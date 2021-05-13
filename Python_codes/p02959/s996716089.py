N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

mons=0
for i in range(N):
  if B[i]>A[i]:
    mons+=A[i]
    if B[i]>=A[i]+A[i+1]:
      mons+=A[i+1]
      A[i+1]=0
    else:
      mons+=B[i]-A[i]
      A[i+1]-=B[i]-A[i]
  else:
    mons+=B[i]
print(mons)