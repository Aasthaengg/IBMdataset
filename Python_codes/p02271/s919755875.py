# coding=utf-8

def solve(i, m):
    global A
    if m == 0:
        ever_calc[i][m] = True
        return True
    elif m < 0:
        ever_calc[i][m] = False
        return False
    elif i == n:
        ever_calc[i][m] = False
        return False
    else:
        result = (solve(i+1, m) or solve(i+1, m-A[i]))
        ever_calc[i][m] = result
        return result

n = int(input())
A = tuple(map(int, input().split()))
q = int(input())
M = tuple(map(int, input().split()))
sum_A = sum(A)
ever_calc = [[None] * 2000 for i in range(n+1)]

for m in M:
    if m > sum_A:
        print('no')
    elif solve(0, m):
        print('yes')
    else:
        print('no')