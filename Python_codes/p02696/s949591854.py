from math import floor
A, B, N = list(map(int, input().split()))
if N < B:
    print(floor(A*N/B)-A*floor(N/B))
else:
    print(floor(A*(B-1)/B)-A*floor((B-1)/B))