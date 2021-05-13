h,w,a,b=[int(_) for _ in input().split()]

ans=[[0 for i in range(w)]for j in range(h)]

for i in range(a,w):
  for j in range(b):
    ans[j][i]=1
for i in range(a):
  for j in range(b,h):
    ans[j][i]=1
    
for i in range(h):
  for j in range(w):
    print(ans[i][j],end="")
  print()