N, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

a.sort()
ans = 0
for i in range(N):
    if x < a[i]:
        x = 0
        break
    x -= a[i]
    ans += 1
if x > 0:
    ans -= 1

print(ans)