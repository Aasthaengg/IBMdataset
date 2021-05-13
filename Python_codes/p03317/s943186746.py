n,k=map(int,input().split())
a=list(map(int,input().split()))
g=1
while k+(k-1)*(g-1)< n:
  g+=1
print(g)