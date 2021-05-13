l = [0]*5
for i in range(3):
  a,b = map(int,input().split())
  l[a]+=1
  l[b]+=1
if max(l) == 3:
  print("NO")
else:
  print("YES")