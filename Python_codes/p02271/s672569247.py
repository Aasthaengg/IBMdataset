n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = map(int, input().split())

memo = {}
def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    if memo.get((i, m), None) == None:
        memo[(i, m)] = solve(i + 1, m) or solve(i + 1, m - A[i])
    return memo[(i, m)]
for m in M:
    if solve(0, m):
        print('yes')
    else:
        print('no')