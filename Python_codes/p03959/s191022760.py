inf = 10 ** 18
mod = 10 ** 9 + 7
n = int(input())
t = [0] + list(map(int, input().split())) + [inf]
a = [inf] + list(map(int, input().split())) + [0]
ans = 1
for i in range(1, n + 1):
    if t[i - 1] < t[i]:
        ans *= 0 if t[i] > a[i] else 1
    if a[i + 1] < a[i]:
        ans *= 0 if t[i] < a[i] else 1
    if t[i - 1] == t[i] and a[i + 1] == a[i]:
        ans *= min(t[i], a[i])
        ans %= mod
print(ans)