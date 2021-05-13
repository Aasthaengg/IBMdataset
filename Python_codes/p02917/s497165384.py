N = int(input())

B = list(map(int,input().split()))

A=[-1 for x in range(N)]
i=0
j=0
for a in B:
  j=i+1
  if A[i]==-1:
    A[i]=a
    A[j]=a
  else:
    if A[i]>a:
      A[i]=a
    A[j]=a
  i=i+1
  #print(A)
total = 0
for num in A:
  total = total + num
print(total)
  
