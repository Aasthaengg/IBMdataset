n = int(input())
s = input()
ans = 0
init = True
m = s.count('#')
l = [0] * m
idx = 0
for i in range(n):
    if s[i] == '#':
        l[idx] = i
        idx += 1
ans = m
for i in range(m):
    ans = min(ans, i + (n - l[i] - 1 - (m - i - 1)))
print(ans)