n=int(input())
lists=[]
for t in range(n):
  a,b=input().split()
  lists.append([a,b])
ans=0
for t in range(n):
  if lists[t][1]=='JPY':
    ans+=int(lists[t][0])
  else:
    ans+=float(lists[t][0])*380000
print(ans)