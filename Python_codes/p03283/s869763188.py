n, m, q = map(int, input().split())

A = [[0]*n for i in range(n)]

for i in range(m):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    A[l][r] += 1

#print(A)

s = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
  for j in range(n):
    s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + A[i][j]

#print(s)

for i in range(q):
    p, q = map(int, input().split())
    p, q = p-1, q-1
    ans = s[q+1][q+1] - s[p][q+1] - s[q+1][p] + s[p][p]
    print(ans)
