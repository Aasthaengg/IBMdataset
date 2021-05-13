N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(N - 1):
    if x >= a[i]:
        ans += 1
        x -= a[i]
    else:
        break

if a[N - 1] == x:
    ans += 1

print(ans)
