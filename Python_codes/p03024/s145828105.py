from sys import stdin
S = stdin.readline().rstrip()
ans = 0
for s in S:
    if s == 'o':
        ans += 1
if ans + (15-len(S)) >= 8:
    print('YES')
else:
    print('NO')
