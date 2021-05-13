n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
tmp=-5
res=0
for i in range(n):
  res += b[a[i]-1]
  if tmp==a[i]-2:
    res += c[a[i]-2]
  tmp=a[i]-1
print(res)