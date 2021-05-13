s = int(input())
MOD = 10**9 + 7
memo = [[0]*(s+1) for _ in range(s//3 + 1)]
flag = True
if s <= 2: flag = False

if flag:
    memo[1] = [0] * 3 + [1] * (s-2)

    for i in range(2, s//3 + 1):
        for j in range(3*i-3, s+1):
            memo[i][j] = memo[i][j-1] + memo[i-1][j-3]

    ans = 0
    for i in range(s//3 + 1):
        ans += memo[i][s]
        ans %= MOD
    print(ans) 
else: print(0)            