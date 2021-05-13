from collections import Counter

n = int(input())
s = str(input())
d = Counter(s)
S = list(set(s))
ans = 1
for t in S:
    ans *= d[t] + 1
print((ans - 1) % (10** 9 + 7))
