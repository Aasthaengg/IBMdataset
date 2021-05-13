n=int(input())
s=input()
a=[0,s.count('R')]
ans=max(a)
for i in range(n):
  if s[i]=='R':
    a[1]-=1
  else:
    a[0]+=1
  ans=min(ans,max(a))
print(ans)