import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().strip()

def main():
    """
    計算量の落とし方が全くわからんので以下のコードを参考に写経。。。
    https://atcoder.jp/contests/abc128/submissions/7712981
    """
    N, Q = map(int, input().split())
    work = []
    for _ in range(N):
        s, t, x = map(int, input().split())
        work.append((x, s - x, t - x))
    work.sort(key=lambda x: (x[0], x[1]))
    start = [int(input()) for _ in range(Q)]

    """
    工事箇所を原点にスライドさせる事で考察を易化しておく。
    各工事(x, s, t)に対して（既にs, tは原点への移動を考慮済み）s<=d<tなるdの個数を求めたい
    startは既に昇順に並んでいるので二分探索でs<=d_i<d_{i+1}<...<d_{j-1}<tなるi=left, j=rightを求める。

    そのあと[left, right)をxで埋めていくが、愚直に(right-left)回xを代入していくとO(Q)かかってTLEするので
    skip[left]=(以前に[left, right)を埋めたときのright)を格納しておく。
    これによりansの表を毎度全走査しなくてもよくなり書き込み範囲のオーバーラップがだいぶ削減される。

    しかしskipを使っても飛んだ先がまたskip命令入ってる可能性もあるから、AC出来るのはやや偶然感あり。。。
    """

    ans = [-1] * Q
    skip = [-1] * Q
    for x, s, t in work:
        left = bisect_left(start, s)
        right = bisect_left(start, t)
        while left < right:
            if skip[left] == -1:
                ans[left] = x
                skip[left] = right
                left += 1
            else:
                left = skip[left]

    for i in range(Q):
        print(ans[i])




if __name__ == "__main__":
    main()
