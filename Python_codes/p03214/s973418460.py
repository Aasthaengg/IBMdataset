import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = [int(x) for x in input().split()]

S = sum(A)
best_diff = 10**18
best_i = -1
for i,x in enumerate(A):
    d = abs(x*N-S)
    if d < best_diff:
        best_diff = d
        best_i = i

print(best_i)