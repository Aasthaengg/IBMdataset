n=int(input())
a=list(map(int,input().split()))
a=[0]+a+[0]
cnt=0
for i in range(1,n+2):
  cnt+=abs(a[i]-a[i-1])

for i in range(1,n+1):
  print(cnt-abs(a[i-1]-a[i])-abs(a[i+1]-a[i])+abs(a[i+1]-a[i-1]))
  
