n,m=map(int,input().split())
l=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  l[a-1]+=1
  l[b-1]+=1
x='YES'
for i in l:
  if i%2:
    x='NO'
    break
print(x)