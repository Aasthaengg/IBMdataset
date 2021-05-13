N = int(input())
l = [[0 for _ in range(10)]for _ in range(10)]

for i in range(1,N+1):
  i = str(i)
  if i[0] == '0' or i[-1] == '0':
    pass
  else:
    l[int(i[0])][int(i[-1])] += 1

ans = 0

for i in range(1,10):
  for j in range(1,10):
    ans += l[i][j]*l[j][i]

print(ans)