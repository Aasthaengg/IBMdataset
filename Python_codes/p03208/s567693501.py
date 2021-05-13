n,k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])

ans = 0
t = float("inf")
for i in range(n-k+1):
  if abs(h[i+k-1] - h[i]) < t:
    t = abs(h[i+k-1] - h[i])
    ans = i

print(h[ans+k-1] - h[ans])