import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from itertools import combinations 
def main():
    N = int(readline())
    L = [int(i) for i in readline().split()]

    #ソートしておく
    L.sort()

    #最長以外の二辺を先に決める
    #インデックスで二辺を選ぶ。最長の辺はjよりインデックスが大きいものとなることが保証される
    #jより後ろでc<a+bとなる最長の辺cの数を求めれば良い。二分探索で条件を満たす最大の辺を見つけるとよい

    #インデックス用の値を用意
    p = [i for i in range(N)]

    #組みを作る
    idxPairs = [(i, j) for i,j in combinations(p, 2)]

    #jよりインデックスが大きい辺の中から最長の辺を見つける
    ans = 0
    for i, j in idxPairs:
        #j以降を二分探索で調べる
        #最長の辺をL[j]と選ぶと必ず三角形を作ることができる
        l = j
        r = N 
        while r-l>1:
            mid = (r+l)//2
            if L[mid] < L[i]+L[j]:
                l = mid
            else:
                r = mid
        ans += l-j
    print(ans)
if __name__ == '__main__':
    main()
