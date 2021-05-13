C=[0,0,0,0]
for _ in range(3):
  a,b=map(int,input().split())
  C[a-1]+=1
  C[b-1]+=1
if 3 in C:
  print("NO")
else:
  print("YES")