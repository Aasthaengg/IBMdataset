import sys
input = sys.stdin.readline

n, p = [int(x) for x in input().split()]
s = input().rstrip()[::-1]
ans = 0
if p == 2:
    for i in range(n):
        if int(s[i]) % 2 == 0:
            ans += (n - i)
    print(ans)
    sys.exit()
if p == 5:
    for i in range(n):
        if int(s[i]) == 0 or int(s[i]) == 5:
            ans += (n - i)
    print(ans)
    sys.exit()
t = [0, int(s[0]) % p]
mul = 10
for i in range(1, n):
    t.append((t[-1] + int(s[i])*mul) % p)
    mul *= 10
    mul %= p
from collections import Counter
c = Counter(t)
for i in c.keys():
    ans += c[i]*(c[i] - 1) // 2
print(ans)

