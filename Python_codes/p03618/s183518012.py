from collections import Counter

A = input()
N = len(A)

c = Counter(A)
ans = 1 + sum(v*(N-v) for v in c.values()) // 2
print(ans)
