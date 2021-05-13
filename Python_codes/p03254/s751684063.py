N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0

for i in range(N):
    x -= a[i]
    if x < 0:
        break
    else:
        ans += 1

if x > 0:
    ans -= 1
else:
    pass

print(ans)