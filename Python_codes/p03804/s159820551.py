n,m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
ans = False
for pattern_h in range(n-m+1):
  for pattern_w in range(n-m+1):
    p = []
    for h in range(m):
      p.append(a[pattern_h+h][pattern_w:pattern_w+m])
    if p==b:
      ans = True
      break
  if ans: break
print('Yes' if ans else 'No')