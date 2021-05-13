n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

d = {'r' : p, 's' : r, 'p' : s}
ans = 0
l = [1] * k + [0] * (n - k)

for i in range(k):
    ans += d[t[i]]

for i in range(k, n):
    if t[i] == t[i - k] and l[i - k]: continue
    ans += d[t[i]]
    l[i] = 1

print(ans)