from collections import Counter

S = list(input())
c = Counter(S)

A = c.get("a", 0)
B = c.get("b", 0)
C = c.get("c", 0)

if max(A, B, C) - min(A, B, C) >= 2:
    print("NO")
else:
    print("YES")
