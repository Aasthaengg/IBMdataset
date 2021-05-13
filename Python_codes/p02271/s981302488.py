n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

table = [[-1 for i in range(max(M)+1)] for j in range(n)]

def solve(i, m):
    if m == 0:
        return True
    elif i >= n:
        return False
    elif table[i][m] != -1:
        return table[i][m]
    elif m - A[i] >= 0:
        res = solve(i + 1, m) or solve(i + 1, m - A[i])
        table[i][m] = res
        return res
    else:
        res = solve(i + 1, m)
        table[i][m] = res
        return res

for m in M:
    if solve(0, m):
        print('yes')
    else:
        print('no')