n, k = map(int, input().split())
h = []
for i in range(n):
  h.append(int(input()))
h.sort()
l = []
for i in range(n - k + 1):
  l.append(h[i + k - 1] - h[i])
print(min(l))