n=int(input())
a=list(map(int,input().split()))
res=[0]*n
temp=0
for i in range(n):
  temp+= a[i]*(-1)**i
res[0]=temp//2
for i in range(1,n):
  res[i]=a[i-1]-res[i-1]
for i in range(n):
  res[i]*=2
print(*res)