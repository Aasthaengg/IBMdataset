def solve(A, i, m, n):
    """Return if it is possible to make value m with some elements in A.

    n is length of A.
    i is index.
    Using Divide-and-Conquer method.
    """

    if m == 0:
        return True
    if i >= n or m < 0:
        return False
    return solve(A, i + 1, m, n) or solve(A, i + 1, m - A[i], n)


import sys

n = int(sys.stdin.readline())
A = tuple(map(int, sys.stdin.readline().split()))
q = sys.stdin.readline()
M = tuple(map(int, sys.stdin.readline().split()))

s_A = sum(A)

ans = ''

for m in M:
    if s_A < m:
        ans += 'no\n'
    elif solve(A, 0, m, n):
        ans += 'yes\n'
    else:
        ans += 'no\n'

print(ans, end = '')