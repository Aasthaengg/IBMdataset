n,p=map(int,input().split())
a=list(map(lambda x:int(x)%2,input().split()))
if a.count(1)==0:
  print((1-p)*2**n)
else:
  print(2**(n-1))