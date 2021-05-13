k,n=map(int,input().split())
for i in range(k-1):
  print(n-k+i+1,end=" ")
print(n,end=" ")
for i in range(k-1):
  print(n+i+1,end=" ")
