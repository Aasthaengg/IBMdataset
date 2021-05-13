n = int(input())
a = list(map(int, input().split()))

ad = sorted([a[i] - i - 1 for i in range(n)])
b = ad[n // 2]

ans = 0
for i in range(n):
    ans += (abs(a[i] - (b + i + 1)))

print(ans)