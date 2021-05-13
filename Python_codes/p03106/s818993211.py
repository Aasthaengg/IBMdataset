A,B,K=map(int,input().split())
k=0
n=min(A,B)
while 1:
  if A%n==0 and B%n==0:
    k+=1
  if K==k:
    break
  n-=1
print (n)
