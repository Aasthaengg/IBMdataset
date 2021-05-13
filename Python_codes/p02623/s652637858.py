n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = [0] * (n + 1)
t = [0] * (m + 1)
for i in range(n):
    s[i+1] = s[i] + a[i]
for i in range(m):
    t[i+1] = t[i] + b[i]

ans = 0
j = m
for i in range(n+1):
    if s[i] > k:
        break
    while s[i] + t[j] > k:
        j -= 1
    ans = max(ans, i + j)
print(ans)