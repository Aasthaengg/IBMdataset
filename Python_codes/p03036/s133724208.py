r, D,x = map(int, input().split())

ans = []
for i in range(10):
  x = x*r-D
  ans.append(x)

for i in range(10):
  print(ans[i])