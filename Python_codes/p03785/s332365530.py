n, c, k = map(int, input().split())
t = []
for i in range(n):
    t.append(int(input()))
t.sort()
ans = 0
counter = 0
lim = t[0]
for i in range(n):
    if counter < c and (t[i] - lim) <= k:
        counter += 1
    else:
        counter = 1
        lim = t[i]
        ans += 1
print(ans + 1)