from collections import Counter

N, M, *AB = map(int, open(0).read().split())

C = Counter(AB)
if any(c % 2 == 1 for c in C.values()):
    print("NO")
else:
    print("YES")
