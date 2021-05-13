n=int(input())
a=list(map(int,input().split()))
n1=max(a)
n2=-n1
nc=n1/2
for m in a:
  if abs(m-nc)<abs(n2-nc) and m!=n1:
    n2=m
print (n1,n2)