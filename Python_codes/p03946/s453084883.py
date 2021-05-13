from collections import Counter
N, T = map(int, input().split())
A = [int(i) for i in input().split()]
m = A[0]
B = []
for a in A[1:]:
    B.append(a - m)
    m = min(m, a)
c = Counter(B)
print(c[max(c.keys())])