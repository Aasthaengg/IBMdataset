n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0

if sum(a) == x:
    print(n)
    exit()

for i in range(n - 1):
    if x >= a[i]:
        ans += 1
        x -= a[i]

print(ans)