n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 1
mod = 10**9 + 7
h = [0 for _ in range(n)]
last = 0
for i in range(n):
    if t[i] != last:
        h[i] = t[i]
        last = t[i]
last = 0
for i in range(n):
    j = n-i-1
    if a[j] != last:
        if (h[j] > 0 and h[j] != a[j]) or a[j] > t[j]:
            ans = 0
            break
        h[j] = a[j]
        last = a[j]
for i in range(n):
    if h[i] == 0:
        ans = ans * min(t[i], a[i]) % mod
print(ans)