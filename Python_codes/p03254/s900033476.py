N, x = map(int, input().split())
an = list(map(int, input().split()))
an.sort()
ans = 0
for a in an:
    x -= a
    if x < 0:
        break
    ans += 1
if x > 0:
    ans -= 1
print(ans)
