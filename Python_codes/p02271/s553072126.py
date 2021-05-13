import sys

n = int(input())
A = list(map(int, sys.stdin.readline()[:-1].split()))

q = int(input())
M = list(map(int, sys.stdin.readline()[:-1].split()))

R = [[None] * 2000 for i in range(n+1)]
def solve(A, n, i, m):
    if R[i][m] != None:
        return R[i][m]
    if m == 0:
        R[i][m] = True
        return True
    if n <= i:
        R[i][m] = False
        return False
    a = A[i]
    R[i][m] = (solve(A, n, i+1, m) or solve(A, n, i+1, m - a))
    return R[i][m]

for m in M:
    if solve(A, n, 0, m):
        print('yes')
    else:
        print('no')