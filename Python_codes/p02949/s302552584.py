N,M,P = map(int, input().split())

es = []

for i in range(M):
    a,b,c = map(int, input().split())
    es.append((a-1, b-1, c))

INF = float("inf")

d = [INF for _ in range(N)] 
d[0] = 0
"""
頂点Nに向かうまでに関係ない閉路に注意する

無限にコインを拾える場合、
・ある閉路を一周したときの得点と支払いの収支がプラス
・その閉路からゴールまで行ける
である。これがない場合、全てのノードを経由してゴールまで行く（N-1回移動）までにコインの枚数が最大になる
なので、一回ベルマンフォード法をやった後もう一回行って一回目と２回目でゴールまでのコイン枚数に変化があればゴ、
ールに行くまでの道に無限にコインをとれる閉路があるといえる

"""

def solve(start, f):
    for i in range(N):
        for a,b,c, in es:
            if d[a] != INF and d[a] + (-c) + P < d[b]:
                # ２週目と区別する。２週目で更新される部分は-INFとか適当に置いておくと、ゴールまでの影響がわかる
                if f == 0:
                    d[b] = d[a] + (-c) + P
                else:
                    d[b] = -INF


    return d[-1]


first=solve(0,0)
second=solve(0, 1)
if first != second:
    print(-1)
else:
    print(max(-first, 0))

