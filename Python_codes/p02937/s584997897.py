s = input()
t = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
n = len(s)
m = len(t)
D = {}
E = {}
for i in range(n):
  if s[i] in D:
    D[s[i]][i] = i
  else:
    D[s[i]] = [-1 for _ in range(n)]
    D[s[i]][i] = i
  E[s[i]] = i
for i in D:
  p = E[i]
  for j in range(E[i], E[i] - n, -1):
    if D[i][(j+n)%n] == -1:
      D[i][(j+n)%n] = p
    else:
      p = j
x = 0
p = 0
for i in range(m):
  if t[i] in D:
    y = D[t[i]][p]
    if y < p:
      x += 1
    if i != m - 1:
      if y == n - 1:
        x += 1
        p = 0
      else:
        p = (y + 1) % n
    else:
      p = y
  else:
    x = -1
    break
if x == -1:
  print(x)
else:
  print(x*n+p+1)