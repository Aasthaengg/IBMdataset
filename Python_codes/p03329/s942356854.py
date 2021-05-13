from collections import defaultdict
import math
N = int(input())
P = defaultdict(int)
def rev(A):
    if A == 0:
        return 0
    elif A in P:
        return P[A]
    else:
        a = int(math.log(A, 9)+10**(-10))
        b = int(math.log(A, 6)+10**(-10))
        if A > 9:
            k = min([rev(A - 9 ** a) + 1, rev(A - 6 ** b) + 1])
            P[A] = k
            return k
        else:
            k = min([rev(A - 9 ** a) + 1, rev(A - 6 ** b) + 1, rev(A - 1) + 1])
            P[A] = k
            return k

print(rev(N))