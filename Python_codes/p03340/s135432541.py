n=int(input())
A=list(map(int,input().split()))
x=[0];s=[0]
for a in A:x.append(x[-1]^a);s.append(s[-1]+a)
l=1;r=1;ans=0
while l<=n:
  while r<=n and x[r]^x[l-1]==s[r]-s[l-1]:r+=1;ans+=1
  l+=1;ans+=r-l
print(ans)