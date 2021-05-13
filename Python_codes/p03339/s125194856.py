n=int(input())
s=input()
ans=n+1
l=[0]*(n+1)
for i in range(n):
  if s[i]=='E':
    l[i+1]=l[i]+1
  else:
    l[i+1]=l[i]
ans=n+1
for i in range(n):
  ans=min(ans,i-l[i]+l[n]-l[i+1])
print(ans)
