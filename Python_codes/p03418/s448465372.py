n,k=map(int,input().split())
result=0
if k==0:
  print(n*n)
  exit()
for i in range(1,n+1):
  result+=max(0,i-k)*(n//i)
  result+=max(0,n%i-k+1)
print(result)
  
