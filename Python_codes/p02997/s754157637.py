import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from itertools import combinations
def main():
    N, K = map(int, readline().split())    
    #全ての2頂点の組合せはN(N-1)/2通り
    #そのうち(N-1)通りは距離1で頂点同士を直接繋いでいる辺である
    #N(N-1)/2 - (N-1) = (N-2)(N-1)/2
    #上記の式より、距離が2以上の2頂点の組合せの数は(N-2)(N-1)/2通り
    #距離が2の頂点数は(N-2)*(N-1)/2以下であるからKがこれより大きいような題意を満たすグラフを構成することはできない
    if K > (N-2)*(N-1)//2:
        print(-1) 
        return 

    #頂点1を根とするスターグラフの頂点1以外の任意の2頂点の最短距離は2である
    #最短距離が2の頂点は(N-1)*(N-2)/2組ある
    #これをK組まで減らすことを考える
    #スターグラフの頂点1以外の2頂点同士に辺を張ることでその頂点間の最短距離を1にすることができる。
    #この操作は他の頂点間の最短距離に影響しない
    #上記の操作を(N-1)*(N-2)//2 - K回行うことで最短距離が2の2頂点の組をKにできる
    M = (N-1)*(N-2)//2 - K
    #N-1はスターグラフの辺の数
    #Mは操作によりスターグラフに追加して張る辺の数
    print(M + N-1) 

    #スターグラフで張る辺を出力
    for i in range(2, N+1):
        print(1, i)

    #あとの操作で張る辺を出力
    #cnt:=操作を行った回数
    cnt = 0
    #頂点2から頂点Nの任意の2頂点の組合せを順に列挙して、操作の対象となる頂点とする
    p = [int(i) for i in range(2, N+1)] 
    for i, j in combinations(p, 2):
        if cnt == M:
            return
        print(i, j)
        cnt += 1
if __name__ == '__main__':
    main()
