from collections import Counter
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
C = Counter(A)
C = sorted(C.values())
r = len(C) - k
if r <= 0:
    print(0)
else:
    print(sum(C[:r]))
