n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(n)]
count = 0
for i in range(n):
  check = c
  for j in range(m):
    check += b[j]*a[i][j]
    if j == m-1:
      if check > 0:
        count += 1
      else:
        pass
print(count)