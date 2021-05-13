import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

S = [None] * N
T = [None] * N
X = [None] * N
for i in range(N):
    S[i], T[i], X[i] = map(int, input().split())

D = [None] * Q
for i in range(Q):
    D[i] = int(input())
    
# X S T
roadworks = [(x, s, t) for x, s, t in zip(X, S, T)]
roadworks = sorted(roadworks, key=lambda x: x[0])
#print(roadworks)

# Dは入力時点でソート済み
walkers = D[:]
ans = [-1] * Q
skip = [-1] * Q

import bisect
for x, s, t in roadworks:
    left = bisect.bisect_left(walkers, s - x)
    right = bisect.bisect_left(walkers, t - x)
    
    i = left
    while i < right:
        if skip[i] == -1:
            ans[i] = x
            skip[i] = right
            i += 1
        else:
            i = skip[i]

    
#print(walkers)
for a in ans:
    print(a)
    




    
    
