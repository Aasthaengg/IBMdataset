n,m=map(int,input().split())

l=[0 for _ in range(n)]

for i in range(m):
  for j in map(int,input().split()):
    l[j-1]+=1

c=0
for i in range(n):
  if l[i]%2==1:
    c+=1
    break

if c==0:
  print("YES")
else:
  print("NO")