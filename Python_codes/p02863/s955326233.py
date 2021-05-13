


N,T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort()


"""
最後に食べる料理は時刻Tを超えても食べていてOKなので、時刻Tの時点で、食べるのに必要な時間が長くても得点の高いものを食べればよい
最後に食べるやつ x N-1品からi番目まで選べる時 x T-1分までのうちt分までに食べ終えて得られる最大のおいしさ
でDPをやると、O(N*N*T)で間に合わない

↑は最後に食べるものを軸に考えたDPだが、実際の所、その後ろの「N-1品～T-1までに食べ終えて得られる最大のおいしさ」を軸にしてみると、
この「」の後に食べる候補で全体の美味しさを最大化できるのは、残りの中で最も美味しいものである。
なので、最後に食べるもののループは実際は必要ない
これでO(N*T)程度になるので間に合う
ただし、食べる時間が速い順に並べおく必要がある。（先にT-1までに食べ終えておくものの中で、最後に食べるのより時間がかかるものがあるなら、入れ替えたほうがよいケースが出てくるので）
"""


dp = [[0 for _ in range(T)] for _ in range(N+1)]

for i in range(N):
    for j in range(T):
        if AB[i][0] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j - AB[i][0]] + AB[i][1])

ans = 0

for i in range(N):
    tmp = 0
    if i < N-1:
        for j in range(i+1, N):
            tmp = max(tmp, AB[j][1])

    ans = max(ans, dp[i+1][-1] + tmp)


print(ans)