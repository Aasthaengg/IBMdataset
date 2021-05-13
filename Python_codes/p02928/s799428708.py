n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
f = 0
d = 0

for i in range(n):
    a.append(a[i])

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            f += 1

for i in range(n):
    for j in range(1, n):
        if a[i] > a[i + j]:
            d += 1

ans = ((f + f + d*(k - 1))*k//2)%mod
print(ans)