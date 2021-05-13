n=int(input())
l=[list(input().split()) for i in range(n)]
ans=0
for i in range(n):
  if l[i][1]=='BTC':
    ans+=float(l[i][0])*380000
  else:
    ans+=int(l[i][0])
print(ans)