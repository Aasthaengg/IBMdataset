N = int(input())
from itertools import groupby, accumulate, product, permutations, combinations
def solve(N):
    pairs = []
    if N%2==1: #和がN
        total = N
        pairs.append([N])
        ans = N-1
    else: #和がN+1
        total = N+1
        ans = 0
    for i in range(1,(total+1)//2):
        pairs.append([i,total-i])
        ans += 2*(N-2)
    print(ans//2)
    for pair1, pair2 in combinations(pairs,2):
        for i in pair1:
            for j in pair2:
                print(i,j)
    return
solve(N)