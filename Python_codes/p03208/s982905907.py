N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort()
diff = max(h)
for i in range(0, len(h)-K+1):
  if diff > h[i+K-1]-h[i]:
    diff = h[i+K-1]-h[i]
print(diff)