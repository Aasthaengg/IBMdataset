N = int(input())
A = list(map(int, input().split()))
table = []

for i, a in enumerate(A):
    table.append([a,i])
table.sort(reverse=True)

# DP[i][j] 左端に i 個, 右端に j 個貪欲に詰めたときのうれしさ
DP = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(1,N+1):
    # i 人目 table[i-1] の幼児を移動させる
    for x in range(i+1):
        y = i - x

        #左端に置く場合と右端に置く場合でmax
        DP[x][y] = max((DP[x-1][y] + table[i-1][0] * abs(table[i-1][1]  - x+1)) * (x>0),\
                     (DP[x][y-1] + table[i-1][0] * abs(table[i-1][1] - (N - y))*(y>0)))


ans = 0
for i in range(N+1):
    for j in range(N+1):
        ans = max(ans, DP[i][j])
print(ans)
