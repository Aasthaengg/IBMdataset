mod = 10 ** 9 + 7

n = int(input())
t = tuple(map(int, input().split()))
a = tuple(map(int, input().split()))

ans = 1
for i in range(1, n - 1):
    x = t[i] if t[i] > t[i - 1] else 1
    y = a[i] if a[i] > a[i + 1] else 1
    ans = ans * max(0, min(t[i], a[i]) - max(x, y) + 1) % mod

print(ans if a[0] == t[-1] else 0)
