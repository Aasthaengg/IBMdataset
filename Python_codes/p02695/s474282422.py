from itertools import combinations_with_replacement
from sys import stdin
input = stdin.readline

N,M,Q = map(int, input().split())
A = [0]*Q
B = [0]*Q
C = [0]*Q
D = [0]*Q
for i in range(Q):
    A[i],B[i],C[i],D[i] = list(map(int, input().split()))

ans = 0
X = [i for i in range(1,M+1)]
for tup in combinations_with_replacement(X,N):
    total = 0
    for i in range(Q):
        if tup[B[i]-1] - tup[A[i]-1] == C[i]:
            total += D[i]
    ans = max(ans,total)

print(ans)