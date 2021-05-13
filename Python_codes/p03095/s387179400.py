N = int(input())
S = input()

from collections import Counter
c = Counter()

for si in S:
    c[si] += 1

# print(c.values())

ans = 1
for n in c.values():
    ans *= n + 1
    ans = ans % (10 ** 9 + 7)

ans -= 1
print(ans)