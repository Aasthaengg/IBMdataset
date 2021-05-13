def i_input(): return int(input())


def i_map(): return map(int, input().split())


def i_list(): return list(i_map())


def i_row_list(N): return [i_list() for _ in range(N)]


n = i_input()
abc = i_row_list(n)
dp=[]
for i in range(n):
    dp.append([0]*3)
dp[0] = abc[0]
for i in range(n):
    if i!=0:
        for j in range(3):
            for k in range(3):
                if j!=k:
                    dp[i][k]=max(dp[i][k],dp[i-1][j]+abc[i][k])

print(max(dp[n-1]))



