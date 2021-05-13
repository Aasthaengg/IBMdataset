def is_pairwise():
    MAX_A = 10**6 + 1
    C = [0] * MAX_A
    for a in A: C[a] += 1
    if sum(C[2::2]) > 1: return False
    for i in range(3, MAX_A, 2):
        if sum(C[i::i]) > 1: return False
    return True

def solve():
    from functools import reduce
    from math import gcd
    if is_pairwise(): return 0
    if reduce(gcd, A) == 1: return 1
    return 2

n = int(input())
A = [*map(int, input().split())]
print(['pairwise','setwise','not'][solve()], 'coprime')
