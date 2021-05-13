a=input().split(" ")
d=100**int(a[0])
k=int(a[1])
ans=d*k
if k==100:
  ans=ans+d
print(ans)