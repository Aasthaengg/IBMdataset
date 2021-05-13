n = int(input())
A = [int(i) for i in input().split()]
input()
M = [int(i) for i in input().split()]

def solve(i, m):
    if m == 0:
        return True
    if i >= n or m < 0:
        return False
    res = solve(i+1, m) or solve(i+1, m-A[i])
    return res

for m in M:
    if sum(A) < m:
        print("no")
    elif solve(0, m):
        print('yes')
    else:
        print('no')
