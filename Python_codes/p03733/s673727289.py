n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=0
T=-1
prev=-1
for i in range(n):
  v=a[i]
  if v<=T:
    T=v+t
  else:
    ans+=(T-prev)
    T=v+t
    prev=v
print(ans+T-prev)