N=int(input())
A=str(input())
B=str(input())
C=str(input())
n=0

for i in range(0,N,1):
  if A[i]==B[i] and A[i]==C[i]:
    n+=0
    continue
  elif A[i]==B[i] or A[i]==C[i] or B[i]==C[i]:
    n+=1
    continue
  else:
    n+=2

print(n)