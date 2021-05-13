n=int(input())
a=[0]+list(map(int,input().split()))+[0]
ans=0
for i in range(n+1):
  ans+=abs(a[i]-a[i+1])
for i in range(1,n+1):
  s=sorted(a[i-1:i+2])
  if a[i]==s[0]:
    print(ans-(s[1]-s[0])*2)
  elif a[i]==s[2]:
    print(ans-(s[2]-s[1])*2)
  else:
    print(ans)