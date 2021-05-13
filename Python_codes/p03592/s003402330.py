n, m, k = map(int, input().split())

judge = [False]*(n*m+1)

for i in range(n+1):
  for j in range(m+1):
    judge[n*j+m*i-i*j*2] = True
if judge[k]:
  print("Yes")
else:
  print("No")