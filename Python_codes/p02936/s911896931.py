
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs2(conj, p=0, t=0, past_p=None, visit=set(), second_visit=set()):   # 距離と探索経路を返す。デクリメントされている場合は、decrement=True にする
    visit.add(p)
    for q in conj[p]:
        if q == past_p:
            # 逆流した際の処理
            continue
        if q in second_visit:
            # 帰り道に訪れた際の処理
            continue
        if q in visit:
            continue
        # p から q への引継ぎ処理
        X[q] += X[p]
        dfs2(conj, q, t+1, p, visit, second_visit)
    second_visit.add(p)
    return X

######################################################################################################

N, Q = map(int, input().split())  # N:頂点数, M:辺

conj = [set() for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1                                    # デクリメントが不要な場合は消す
    v -= 1
    conj[u].add(v)
    conj[v].add(u)                            # 無効グラフの場合は消す

X = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    X[p-1] += x

print(*dfs2(conj, p=0))