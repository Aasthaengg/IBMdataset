N=int(input())
A=[]
A_before=input().split(' ')
for i in range(len(A_before)):
  A.append(int(A_before[i]))
for i in range(len(A)):
  for j in range(len(A)-1):
    if A[j]<A[j+1]:
      x=A[j]
      A[j]=A[j+1]
      A[j+1]=x
a=0
b=0
for i in range(len(A)):
  if i%2==0:
    a=a+A[i]
  else:
    b=b+A[i]
print(a-b)
