n=int(input())
a=list(map(int,input().split()))
a.sort()
A=[a[0]]
x=0
sum=sum(a)
sumL=-9999999999
if n==2:
  print(max(a)-min(a))
  print(max(a),min(a))
else:
  for i in range(1,n):
    A.append(A[i-1]+a[i])
  for i in range(1,n):
    if sumL<-A[i-1]+sum-A[i-1]:
      sumL=-A[i-1]+sum-A[i-1]
      x=i
  print(sumL)
  L1=a[0:x]
  L2=a[x:n]

  if x!=1:
    print(L2[0],L1[0])
    z=L2[0]-L1[0]
    for i in range(1,x-1):
      print(z,L1[i])
      z=z-L1[i]
  else:
    z=L2[0]

  if x!=n-1:
    print(L1[x-1],L2[1])
    y=L1[x-1]-L2[1]
    for i in range(2,len(L2)):
      print(y,L2[i])
      y=y-L2[i]
  else:
    y=L1[len(L1)-1]

  print(z,y)