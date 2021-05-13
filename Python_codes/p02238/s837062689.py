def visit(u):
  global t
  flag[u] = 1
  t += 1
  s[u] = t
  for v in range(n):
    if M[u][v]==0:
      continue
    if flag[v]==0:
      visit(v)
  flag[u] = 2
  t += 1
  e[u] = t


def dfs():
  for u in range(n):
    if flag[u]==0:
      visit(u)
  for u in range(n):
    print '%d %d %d' % (u+1, s[u], e[u])


n = input()
t = 0
flag = [0 for row in range(n)]
s = [0 for row in range(n)]
e = [0 for row in range(n)]
M = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
  str = map(int, raw_input().split())
  u = str[0]
  k = str[1]
  a = str[2:]
  u -= 1
  for v in a:
    M[u][v-1] = 1

dfs()