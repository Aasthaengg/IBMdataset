from pprint import pprint
def main():
    D,G = map(int, input().split())
    p,c = [0]*D,[0]*D
    for i in range(D):
        p[i],c[i] = map(int, input().split())
    qnum = sum(p)
    # dp[i][j] := i問目まででj個解いたときの最大得点
    dp = [[0]*(qnum+1) for _ in range(D+1)]
    dp[0] = [0]*(qnum+1)
    ans = qnum
    for i in range(1,D+1):
        # i問目までを見る
        for j in range(qnum+1):
            # 全部でj回解く
            for k in range(min(p[i-1]+1, j+1)):
                # i問目をk個解く
                if k<p[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-k]+100*i*k)
                else:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-k]+100*i*k+c[i-1])
                if dp[i][j]>=G:
                    ans = min(ans, j)
    pprint(ans)

main()
