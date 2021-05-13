n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
ans = 0
for i in range(1, n + 1):
    if i == a[a[i]]:
        ans += 1
ans //= 2
print(ans)