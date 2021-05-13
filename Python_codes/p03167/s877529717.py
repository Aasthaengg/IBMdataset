h, w = map(int, input().split())
A = [input() for _ in range(h)]
mod = 10**9 + 7
memo = [[0] * w for _ in range(h)]
for i in range(h):
    if A[i][0] == '.':
        memo[i][0] = 1
    else:
        break
for j in range(w):
    if A[0][j] == '.':
        memo[0][j] = 1
    else:
        break
for i in range(1, h):
    for j in range(1, w):
        if A[i][j] == '#':
            memo[i][j] = 0
        else:
            memo[i][j] = (memo[i-1][j] + memo[i][j-1]) % mod
print(memo[-1][-1])