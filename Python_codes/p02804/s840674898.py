n, k = map(int, input().split())
a = [int(i) for i in input().split()]
Mod = 10**9 + 7
a.sort()
c = [0] * (n+1)
c[k - 1] = 1
for i in range(n+1):
    if i >= k:
        c[i] = ((c[i - 1]*i * pow(i - k + 1, Mod - 2, Mod))) % Mod
ans = 0
for i in range(1, n + 1):
    ans += (a[i - 1] * (c[i - 1] - c[n - i])) % Mod
print(ans % Mod)