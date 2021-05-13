n,k=map(int,input().split())
a=list(map(int,input().split()))
n-=k
k-=1
count=1

if n<=0:
  pass
else:
  while n>0:
    n-=k
    count+=1
    
print(count)