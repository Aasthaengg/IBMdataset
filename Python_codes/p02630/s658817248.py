from collections import defaultdict

N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())
B = []
C = []
for _ in range(Q):
    b, c = [int(s) for s in input().split()]
    B.append(b)
    C.append(c)

A_dict = defaultdict(int)
for a in A:
    A_dict[a] += 1

A_sum = sum(A)
for b, c in zip(B, C):
    n = A_dict[b]
    A_dict[b] = 0
    A_dict[c] += n
    A_sum += (c - b) * n
    print(A_sum)
