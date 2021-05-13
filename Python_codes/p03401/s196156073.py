n=int(input())
a=list(map(int,input().split()))
ans=0
temp=0
for i in range(n):
  ans=ans+abs(a[i]-temp)
  temp=a[i]
ans=ans+abs(temp)
a.insert(0,0)
a.append(0)
for i in range(1,n+1):
  print(ans-abs(a[i]-a[i-1])-abs(a[i+1]-a[i])+abs(a[i+1]-a[i-1]))