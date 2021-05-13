N = int(input())
A = list(map(int, input().split()))
Q = int(input())
m = list(map(int, input().split()))
memo = [[-1]*2000 for _ in range(20)]
def solve(i, m):
    if memo[i][m] != -1:
        return memo[i][m]
    if m == 0:
        memo[i][m] = 1
        return True
    if m < 0:
        memo[i][m] = 0
        return False
    if i >= N:
        memo[i][m] = 0
        return False
    if i == N-1:
        memo[i][m] = (A[N-1] == m)
        return (A[N-1] == m)
    res = solve(i+1, m) or solve(i+1, m-A[i])
    memo[i][m] = res
    return res
for mi in m:
    if solve(0, mi):
        print("yes")
    else:
        print("no")
