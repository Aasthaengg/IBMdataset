s=input()
n=len(s)
ans=0
cnt=0
for i in range(n):
  if s[i]=='W':
    ans+=i-cnt
    cnt+=1
print(ans)