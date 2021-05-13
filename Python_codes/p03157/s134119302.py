h, w = map(int, input().split())
s = []
for _ in range(h):
  s.append(input().strip())

visited = [[False for _ in range(w)] for _ in range(h)]

ans = 0
for i in range(h):
  for j in range(w):
    if visited[i][j]:
      continue
    bc = 0
    wc = 0
    visited[i][j] = True
    node = [(i, j)]
    while node:
      ci, cj = node[0]
      node = node[1:]
      if s[ci][cj] == '#':
        bc += 1
      else:
        wc += 1
      if ci - 1 >= 0 and s[ci][cj] != s[ci-1][cj]:
        if not visited[ci-1][cj]:
          visited[ci-1][cj] = True
          node.append((ci-1, cj))
      if ci + 1 <= h-1 and s[ci][cj] != s[ci+1][cj]:
        if not visited[ci+1][cj]:
          visited[ci+1][cj] = True
          node.append((ci+1, cj))
      if cj - 1 >= 0 and s[ci][cj] != s[ci][cj-1]:
        if not visited[ci][cj-1]:
          visited[ci][cj-1] = True
          node.append((ci, cj-1))
      if cj + 1 <= w-1 and s[ci][cj] != s[ci][cj+1]:
        if not visited[ci][cj+1]:
          visited[ci][cj+1] = True
          node.append((ci, cj+1))
    ans += bc * wc

print(ans)
