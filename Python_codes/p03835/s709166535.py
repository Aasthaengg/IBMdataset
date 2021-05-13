s,t=map(int,input().split())
ans=0
for i in range(0,s+1,1):
  for j in range(0,s+1,1):
    if not s<t-i-j and not 0>t-i-j:
      ans+=1
print(ans)