import sys
from heapq import *
def input(): return sys.stdin.readline().strip()


def main():
    """
    文字列のソートをする際には計算量に要注意！
    数字の大小比較と違って文字列の比較の場合は１文字１文字左から順番に見ないといけない。
    そのため一回の比較でO(比較文字列の長さ)分の計算量がかかる。
    特に長さMの文字列N個をソートするのにかかる時間は
            ❌O(NlogN)
            ⭕️O(MNlogN)

    そこで文字列のソート時には文字数をなるべく小さくするのがポイント。
    今回K<=5なので、「答えはK<=5文字以下になる」のがミソ。
    """

    s = input()
    L = len(s)
    K = int(input())
    string = set([])
    for i in range(L):
        for j in range(i + 1, min(i + K, L) + 1):
            string.add(s[i:j])

    string = list(string)
    heapify(string)
    for _ in range(K):
        ans = heappop(string)
    print(ans)


if __name__ == "__main__":
    main()
