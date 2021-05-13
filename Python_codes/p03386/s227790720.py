from itertools import chain
A, B, K = map(int, input().split())
L = range(A, B + 1)
if K < (B - A + 2) // 2:
    L = chain(L[:K], L[-K:])
print("\n".join(str(i) for i in L))