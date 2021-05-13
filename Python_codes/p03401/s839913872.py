n=int(input())
a=list(map(int,input().split()))
total=0
for i in range(n-1):
  total+=abs(a[i+1]-a[i])
total+=(abs(a[0])+abs(a[n-1]))
for i in range(n):
  if i==0:
    print(total-abs(a[1]-a[0])-abs(a[0])+abs(a[1]))
  elif i!=n-1:
    print(total-abs(a[i+1]-a[i])-abs(a[i]-a[i-1])+abs(a[i+1]-a[i-1]))
  else:
    print(total-abs(a[n-1]-a[n-2])-abs(a[n-1])+abs(a[n-2]))