n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

if n <= k:
    ans = 0
else:
    ans = sum(h[:n-1*k])

print(ans)

