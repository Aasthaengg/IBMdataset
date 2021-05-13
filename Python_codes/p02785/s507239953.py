n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

h = h[::-1]
h = h[k:]

ans = sum(h)

print(ans)