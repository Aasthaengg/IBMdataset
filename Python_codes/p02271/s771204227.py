n = int(input())
A = list(sorted(map(int, input().split())))
q = int(input())
M = list(map(int, input().split()))

R = [[None] * 2000 for i in range(n + 1)]

def solve(A, i, m, n):
    if R[i][m] != None:
        return R[i][m]
    if m == 0:
        R[i][m] = True
        return True
    elif i >= n:
        R[i][m] = False
        return False
    else:
        ans = solve(A, i + 1, m, n) or solve(A, i + 1, m - A[i], n)
        R[i][m] = ans
        return ans

for i in M:
    if sum(A) < i:
        print('no')
    elif solve(A, 0, i, n):
        print('yes')
    else:
        print('no')