n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

same = 0
for i, ei in enumerate(a):
    for j, ej in enumerate(a[i+1:], i + 1):
        if ei > ej:
            same += 1
            same %= mod

other = 0
for ei in a:
    for ej in a:
        if ei > ej:
            other += 1
            other %= mod

ans = same * k + other * k * (k - 1) // 2
ans %= mod
print(ans)
