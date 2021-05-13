# 解説AC
# 参考1: https://drken1215.hatenablog.com/entry/2019/09/29/103500
# 参考2: https://www.slideshare.net/chokudai/wap-atcoder4


n, m = map(int, input().split())
A, B, C = [], [], []
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    c = list(map(int, input().split()))
    now = 0
    for i in range(b-1, -1, -1):
        now += 2**(c[i]-1)
    C.append(now)

INF = 10**9
DP = [[INF for _ in range(2**n)] for _ in range(m+1)]
DP[0][0] = 0

for i in range(m):
    for j in range(2**n):
        c = C[i]
        # 鍵を使用しない
        DP[i+1][j] = min(DP[i][j], DP[i+1][j])
        # 鍵を使用する
        nex = j | c
        DP[i+1][nex] = min(DP[i+1][nex], DP[i][j]+A[i])

ans = 10**9
for i in range(m):
    ans = min(DP[i][-1], ans)

if ans == 10**9:
    ans = -1

print(ans)