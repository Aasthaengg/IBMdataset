n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=0
for i in range(n):
  if a[i]>=b[i]:
    cnt+=b[i]
    a[i]-=b[i]
    b[i]=0
  elif a[i]<b[i]:
    cnt+=a[i]
    b[i]-=a[i]
    a[i]=0
    temp=b[i]
    cnt+=min(b[i], a[i+1])
    b[i]=max(b[i]-a[i+1], 0)
    a[i+1]=max(a[i+1]-temp, 0)
print(cnt)