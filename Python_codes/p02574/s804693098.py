MAX_A = 10**6 + 1

def prim_gen():
    num = [i%2==1 for i in range(MAX_A)]
    num[0] = False; num[2] = True
    prim = set()
    prim.add(2)
    for i in range(3, MAX_A, 2):
        if num[i]: prim.add(i)
        for j in range(i+i, MAX_A, i): num[j] = False
    return prim

def solve():
    C = [0] * MAX_A
    for a in A: C[a] += 1
    pairwise = True
    for p in prim:
        if sum(C[p:MAX_A:p]) > 1: pairwise = False
    if pairwise: return 'pairwise'
    from math import gcd
    g = 0
    for a in A: g = gcd(g, a)
    if g == 1: return 'setwise'
    return 'not'

n = int(input())
A = [*map(int, input().split())]
prim = prim_gen()
print(solve(), 'coprime')
