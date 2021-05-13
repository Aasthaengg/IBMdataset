n,k=map(int,input().split());result=0
for i in range(1,n+1):
  t=i
  count=0
  while t < k:
    t*=2
    count+=1
  result+=1/n*1/2**count
print(result)