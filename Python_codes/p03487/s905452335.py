n=int(input())
a=list(map(int,input().split()))
t={}
for i in range(n):
  if a[i] in t:
    t[a[i]]+=1
  else:
    t[a[i]]=1
ans=0
for i in t:
  if i>t[i]:
    ans+=t[i]
  else:
    ans+=t[i]-i
print(ans)