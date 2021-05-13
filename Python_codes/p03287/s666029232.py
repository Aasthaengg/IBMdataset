n, m = map(int, input().split())
a = list(map(int, input().split()))
memo = [0]
d = {0: 1}
for ai in a:
  memo.append((memo[-1] + ai) % m)
  mi = memo[-1]
  if mi in d:
    d[mi] += 1
  else:
    d[mi] = 1
ans = 0
for k in d:
  c = d[k]
  ans += c * (c-1) // 2
print(ans)
  
