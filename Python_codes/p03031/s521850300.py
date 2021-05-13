n, m  = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
d = [0]*(n+1)
s = 0
for i in range(2**n):
  for j in range(n):
    if i & (1<<j):
      d[j+1] = 1
    else:
      d[j+1] = 0
  for k in range(m):
    a = 0
    for l in range(1, lst[k][0]+1):
      a = (a+d[lst[k][l]])%2
    if a!=p[k]:
      break
  else:
    s += 1

print(s)