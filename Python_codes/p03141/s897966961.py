N = int(input())
prefs = []
for i in range(N):
    a, b = map(int, input().split())
    prefs.append((a + b, a, b))
prefs.sort(reverse=True)
ans = 0
for i, (p, a, b) in enumerate(prefs):
    if i % 2:
        ans -= b
    else:
        ans += a
print(ans)
