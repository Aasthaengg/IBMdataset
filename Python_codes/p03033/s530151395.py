# ref https://www.owlog.org/abc128/

import sys
sys.setrecursionlimit(10 ** 7)
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    # 通行止めの地点 (X,S,T)
    closure = []
    for _ in range(N):
        start, end, pos = map(int, input().split())
        closure.append((pos, start, end))

    # 座標の昇順でソート
    closure.sort()

    D = [int(input()) for _ in range(Q)]

    # 各人の止まる地点
    ans = [-1] * Q
    # その人が既に止まっているか
    skip = [-1] * Q

    # 各通行止めの地点で止まる人を探索
    # Dが範囲[S-X,T-X)にあるときに止まる
    for pos, start, end in closure:
        # 一番左の人のインデックス
        left = bisect_left(D, start - pos)
        # 一番右の人のインデックス
        right = bisect_left(D, end - pos)

        while left < right:
            if skip[left] == -1:
                # 停止座標を記録
                ans[left] = pos
                # 右端の人のインデックスを記録
                skip[left] = right
                left += 1
            else:
                # [left,skip[left])にいる人は既に止まっている
                left = skip[left]

    return ans


if __name__ == '__main__':
    print(*main(), sep='\n')