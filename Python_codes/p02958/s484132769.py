n = int(input())
p = list(map(int, input().split()))
s = sorted(p)
c = 0
for i in range(len(p)):
    if p[i] == s[i]:
        c += 1
if c >= len(p)-2:
    print('YES')
else:
    print('NO')