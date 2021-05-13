N = int(input())
A = list(map(int, input().split()))
B = set(A)
d = {}
for a in A:
  d[a] = d.get(a, 0) + 1
ans = 0
for b in B:
  s = d[b]
  if s >= b:
    ans += (s - b)
  else:
    ans += s
print(ans)