N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

xyz = [[0]*3 for _ in range(N+1)]

ans = 1
for i in range(1, N+1):
    plus_flg = True
    tmp = 0
    for j in range(3):
        xyz[i][j] = xyz[i-1][j]
        if xyz[i-1][j] == A[i-1]:
            tmp += 1
            if plus_flg:
                xyz[i][j] = xyz[i-1][j] + 1
                plus_flg = False
    ans *= tmp
    ans %= MOD

print(ans)