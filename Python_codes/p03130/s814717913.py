c=[0]*5
for i in range(3):
  a,b=map(int,input().split())
  c[a]+=1
  c[b]+=1
if 3 in c:
  print("NO")
else:
  print("YES")