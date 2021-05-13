n, m = map(int, (input().split()))
b = []
for _ in range(n):
    a = list(map(int, input().split()))
    b.extend(a[1:])

ans = 0
for i in range(1,31):
    if b.count(i) == n:
        ans += 1
print(ans)