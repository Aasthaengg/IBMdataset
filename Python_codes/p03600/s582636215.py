# https://atcoder.jp/contests/abc074/tasks/arc083_b

# 考えること
# 1, どうやったらu→vの最短経路を復元できるか？
# 2, そのような道路が存在しない場合とはどういうときか？

# 重要な考察
# 1, iを固定したとき、j=arg_j min D[i][j] はiと必ず隣接する
# 2, d(u,v)=d(u,i)+d(i,v) を満たすiは最短経路の中にある。


# minimum sppaning treeからスタートする発想は悪くなかったねぇ

# 解説見ました...

# 道路が存在しない場合の判別方法→隣接行列Aに対してワーシャルフロイドをして、隣接行列Bを作成
# B(u,v)<A(u,v)となるとき、理想の最短距離よりも短い最短距離が存在して矛盾が生じるので-1

# Aを全点間グラフとして、辺の削除を考える。
# あらゆる二点に関するminimumな経路は？u,i,vについて、d(u,v)<d(u,i)+d(i,v)ならば、辺を残さないと最小距離にならない.
# 逆にd(u,v)=d(u,i)+d(i,v)ならば、d(u,v)の方は取り除いても構わない  (d(u,v)>d(u,i)+d(i,v)の状況はワーシャルフロイドで取り除かれている)


import sys
read = sys.stdin.readline
ra = range
enu = enumerate


def read_a_int():
    return int(read())


def read_matrix(H):
    '''
    H is number of rows
    '''
    ret = []
    for _ in range(H):
        ret.append(list(map(int, read().split())))
    return ret
    # return [list(map(int, read().split())) for _ in range(H)] # 内包表記はpypyでは遅いため


N = read_a_int()
A = read_matrix(N)
from itertools import combinations
edge_rm = set()
for u, v in combinations(range(N), 2):
    for i in range(N):
        if i == u or i == v:
            continue
        a = A[u][i]
        b = A[i][v]
        c = A[u][v]
        # print(a, b, c)
        if c == a + b:
            # print(u, i, v, a, b, c)
            edge_rm.add((u, v) if u < v else(v, u))
        elif c > a + b:
            print(-1)
            exit()
# print(edge_rm)
ans_sum = 0
for a in A:
    for aa in a:
        ans_sum += aa
ans_sum //= 2
for u, v in edge_rm:
    ans_sum -= A[u][v]
print(ans_sum)
