n,k = map(int,input().split())
h = list(int(input()) for i in range(n))
h.sort()
p = max(h) - min(h)

for i in range(n - k + 1):
    p = min(p,h[i + k - 1] - h[i])

print(p)