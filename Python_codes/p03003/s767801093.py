
N,M = map(int,input().split())

S = list(map(int,input().split()))
T = list(map(int,input().split()))


ans = [[0] * (M+1) for i in range(N+1)]

for i in range(N+1):

    for j in range(M+1):

        if i == 0 or j == 0:
            ans[i][j] = 1

        elif S[i-1] == T[j-1]:
            ans[i][j] = ans[i-1][j] + ans[i][j-1]

        else:
            ans[i][j] = ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1]

        ans[i][j] %= (10 ** 9 + 7)

print (ans[-1][-1])
