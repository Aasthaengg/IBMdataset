from collections import Counter
A = list(input())
N = len(A)
cA = Counter(A)
dpl = 0
for i in cA.values():
  dpl += i * (i - 1) // 2
print(N * (N - 1) // 2 - dpl + 1)