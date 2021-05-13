n,h,w=map(int,input().split())
ans=0
for i in range(n):
  s,t=map(int,input().split())
  ans+=(s>=h and t>=w)
print(ans)