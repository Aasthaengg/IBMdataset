import sys
input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
if N == 2 or M == 2:
    print(0)
elif N == 1 and M == 1:
    print(N * M)
elif N == 1:
    print(M-2)
elif M == 1:
    print(N-2)
else:
    print(((N-2) * (M-2)))