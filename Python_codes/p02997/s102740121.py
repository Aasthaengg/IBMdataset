#ABC131-E Friendships
"""
問題：
頂点数n,辺数mとして最短距離が2となる辺がk個となる
重みなし無向グラフが存在するかを調べる。
解法：
まず、うにグラフの状態がkの最大値であることが言える。
(うにグラフ…頂点1に全ての頂点を繋いだ状態。n-1辺になる。)
この時のkは2頂点の組み合わせ数(n-1)C2なので、これを超えるkは
満たせず、そうでなければ適当な2頂点を繋げばそれ以下の値を全て
満たせることになる。(二頂点を繋いでも他の辺の最短距離に影響しない)
"""
import sys
import itertools
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,k = map(int,readline().split())

#二項係数(modなし) O(k)
def large_conbination(n,k): #no mod. return nCk.
    res1 = 1
    for i in range(n,n-k,-1):
        res1*=i
    res2 = 1
    for i in range(1,k+1):
        res2*= i
    return res1//res2

mx = large_conbination(n-1,2) #うにグラフ状態

if k > mx:
    print(-1)
else:
    graph = []
    for i in range(1,n):
        graph.append((1,i+1)) #うにグラフの作成
    count = 0
    for i in itertools.combinations([i for i in range(2,n+1)],2):
        if k == mx-count:
            break
        graph.append(i)
        count += 1
    print(len(graph))
    for i,j in graph:
        print(i,j)