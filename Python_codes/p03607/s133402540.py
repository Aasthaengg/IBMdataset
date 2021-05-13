from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]
C = Counter(A)
c = 0
for k, v in C.items():
    if v % 2 == 1:
        c += 1
print(c)