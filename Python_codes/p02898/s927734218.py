n, k = map(int, input().split())
h = list(map(int, input().split()))
res = 0
for h_k in h:
  if h_k >= k:
    res += 1

print(res)