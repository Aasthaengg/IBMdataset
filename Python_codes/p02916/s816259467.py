n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
ful=0
for i in range(n):
  tempa=A[i]-1
  ful+=B[tempa]
  if A[i]-A[i-1]==1 and i>0:
    tempb=A[i-1]-1
    ful+=C[tempb]
print(ful)