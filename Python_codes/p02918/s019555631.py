n, k = map(int, input().split())
s = input()
d = 0
for c1, c2 in zip(s, s[1:]):
    if c1 == 'R' and c2 == 'L':
        d += 1
e = 0
if s[0] == 'L':
    e += 1
if s[-1] == 'R':
    e += 1
k, d = max(k - d, 0), max(0, d - k)
if k > 0:
    e = 1
ans = max(0, n - d * 2 - e)
print(ans)
