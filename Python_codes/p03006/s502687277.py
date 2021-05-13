n = int(input())
A = []
for _ in range(n):
  x, y = map(int, input().split())
  A.append((x, y))
maxc = 0
for i in range(n):
  for j in range(n):
    c = 0
    if i == j:
      continue
    dx = A[i][0] - A[j][0]
    dy = A[i][1] - A[j][1]
    for k in range(n):
      for l in range(n):
        if k == l:
          continue
        if A[k][0] + dx == A[l][0] and A[k][1] + dy == A[l][1]:
          c += 1
    if maxc < c:
      maxc = c
print(n-maxc)
    
    

