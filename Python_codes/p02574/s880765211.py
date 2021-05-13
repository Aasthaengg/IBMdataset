MAX_A = 10**6 + 1
MAX_P = MAX_A // 2
is_prim = [i%2==1 for i in range(MAX_P)]
is_prim[1] = False; is_prim[2] = True
for i in range(3, MAX_P):
    if not is_prim[i]: continue
    for j in range(i+i, MAX_P, i): is_prim[j] = False

def solve():
    C = [0] * MAX_A
    for a in A: C[a] += 1
    pairwise = True
    for p in [i for i in range(MAX_P) if is_prim[i]]:
        if sum(C[p::p]) > 1: pairwise = False
    if pairwise: return 'pairwise'
    from math import gcd
    g = 0
    for a in A: g = gcd(g, a)
    if g == 1: return 'setwise'
    return 'not'

n = int(input())
A = [*map(int, input().split())]
print(solve(), 'coprime')
