# coding=utf-8

def solve(i, m):
    global A
    if m == 0:
        return True
    elif i == n:
        return False
    else:
        return (solve(i+1, m) or solve(i+1, m-A[i]))

n = int(input())
A = tuple(map(int, input().split()))
q = int(input())
M = tuple(map(int, input().split()))
sum_A = sum(A)

for m in M:
    if m > sum_A:
        print('no')
    elif solve(0, m):
        print('yes')
    else:
        print('no')