

N, M = map(int, input().split())

es = []
for i in range(M):
    a,b,c = map(int, input().split())
    es.append((a-1, b-1, c))

INF = float("inf")
d = [INF] * N
d[0] = 0
"""
最大経路探索的な問題
よくあるベルマンフォード法なら、コストが正の値で、負の閉路が見つかったら失敗、という形で最小経路を求めることになる。
今回は最長経路なので、正の閉路が求まったら失敗にしたい。
なので
・コストを負の値でもつ。表示するときに正に変える
・コストを負にするので閉路を見つけられる
みたいな形にする
"""

def solve(start):
    for i in range(N):
        for a,b,c, in es:
            if d[a] != INF and d[a] + (-c) < d[b]:
                d[b] = d[a] + (-c)
                # 最後まで確認しても更新されたら閉路あり
                if i == N-1 and b == N-1:
                    return "inf"

    return -1*d[-1]

print(solve(0))