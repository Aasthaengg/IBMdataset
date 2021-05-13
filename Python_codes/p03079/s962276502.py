from sys import stdin

A, B, C = list(map(int, stdin.readline().split()))

if A == B  and B == C and A == C:
    print('Yes')
else: print('No')
