n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

n += 1
ans = 0
m = dict()
temp = 0
b = []
for i in range(min(n, k)):
    temp = (temp + a[i]) % k
    c = (temp - (i % k) + k) % k
    b.append(c)
    if c in m.keys():
        ans += m[c]
        m[c] += 1
    else:
        m[c] = 1

for i in range(k, n):
    x = i % k
    m[b[x]] -= 1
    temp = (temp + a[i]) % k
    c = (temp - (i % k) + k) % k
    b[x] = c
    if c in m.keys():
        ans += m[c]
        m[c] += 1
    else:
        m[c] = 1

print(ans)
