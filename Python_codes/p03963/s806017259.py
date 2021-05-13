balls, colors = map(int,input().split())

ans = 1

for i in range(1,balls+1):
  if i == 1:
    ans *= colors
  else:
    ans *= colors - 1

print(ans)