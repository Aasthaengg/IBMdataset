n=int(input())
l=[None]*n
for i in range(n):
  a,b=map(int,input().split())
  l[i]=[a,b]
l.sort(key=lambda x:x[0]+x[1], reverse=True)
#print(l)
ans=0
for i in range(n):
  if i%2:
    ans-=l[i][1]
  else:
    ans+=l[i][0]
print(ans)