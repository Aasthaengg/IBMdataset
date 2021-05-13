n, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 0
for a in A:
    x -= a
    if x < 0:
        break
    else:
        ans += 1
if 0 < x:
    ans -= 1

print(max(ans, 0))
