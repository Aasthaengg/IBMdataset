n = int(input())
p = [int(input()) for _ in range(n)]
s = [0] * n
for i in range(n):
    s[p[i] - 1] = i
ans = 0
m = s[0]
c = 0
for i in s:
    if i >= m:
        c += 1
    else:
        ans = max(ans, c)
        c = 1
    m = i
ans = max(ans, c)
print(n - ans)