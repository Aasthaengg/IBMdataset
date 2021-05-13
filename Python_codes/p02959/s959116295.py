n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

cnt=0

for i in range(n):
  if a[n-i]>=b[n-1-i]:
    cnt+=b[n-1-i]
  else:    
    if a[n-1-i]-(b[n-1-i]-a[n-i])>=0:
      a[n-1-i]-=b[n-1-i]-a[n-i]
      cnt+=b[n-1-i]
    else:
      cnt+=a[n-i]+a[n-1-i]
      a[n-1-i]=0
      
print(cnt)
