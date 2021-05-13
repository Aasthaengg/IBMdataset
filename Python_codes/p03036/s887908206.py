r,d,x = map(int,input().split())

ans = []
tmp = r*x - d
ans.append(tmp)
print(tmp)
for i in range(0,9):
  x_i = ans[i]
  tmp = r*x_i - d
  ans.append(tmp)
  print(tmp)