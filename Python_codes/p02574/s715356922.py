n = int(input())
A = [*map(int, input().split())]
def solve():
    MAX_A = 10**6 + 1
    C = [0] * MAX_A
    for a in A: C[a] += 1
    pairwise = True
    if sum(C[2::2]) > 1: pairwise = False
    for i in range(3, MAX_A, 2):
        if sum(C[i::i]) > 1: pairwise = False
    if pairwise: return 'pairwise'
    from math import gcd
    g = 0
    for a in A: g = gcd(g, a)
    if g == 1: return 'setwise'
    return 'not'
print(solve(), 'coprime')
