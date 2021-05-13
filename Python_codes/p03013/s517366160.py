n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
mod = int(1e9 + 7)
one_or_two = [0] + [1] + [2] + [-1] * n
for i in range(3, n + 3):
    one_or_two[i] = (one_or_two[i-1] + one_or_two[i-2]) % mod
if m == 0:
    print(one_or_two[n])
    exit()
ans = 1
if a[0] > 1:
    ans *= one_or_two[a[0]-1]
for i in range(1, m):
    if a[i] - a[i-1] == 2:
        continue
    if a[i] - a[i-1] == 1:
        ans = 0
        break
    ans *= one_or_two[a[i] - a[i-1] - 2]
    ans %= mod
if n - a[-1] > 1:
    ans *= one_or_two[n - a[-1] - 1]
print(ans % mod)