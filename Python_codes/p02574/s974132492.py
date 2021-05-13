def gcd_all(a):
    from math import gcd
    g = 0
    for x in a: g = gcd(g, x)
    return g

def is_pairwise():
    MAX_A = 10**6 + 1
    C = [0] * MAX_A
    for a in A: C[a] += 1
    for i in range(2, MAX_A):
        if sum(C[i::i]) > 1: return False
    return True

def solve():
    if is_pairwise(): return 'pairwise'
    if gcd_all(A) == 1: return 'setwise'
    return 'not'

n = int(input())
A = [*map(int, input().split())]
print(solve(), 'coprime')
