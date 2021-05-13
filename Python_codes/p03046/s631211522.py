import sys
def input(): return sys.stdin.readline().strip()

def main():
    M, K =map(int, input().split())
    k = bin(K)[2:]

    """
    構成問題無理です。。。。。。
    K < 2^Mを最初にちゃんと定式化しておけば、Mに関して場合分けしたくなるのか？
    （Kで場合分けして詰んだ人）

    そしてどっちみちM=2で実験しても定式化できんかった。。。。。。
    「K以外の0以上2M未満の整数を昇順に並べた数列をbとします。またbの逆順をcとします。
    このとき bKcK と並べてできる数列をaとすればよいです。」
    →言われれば納得するけどなあ

    0 ¥oplus 1 ¥oplus ... ¥oplus (2^M-1) = 0　(M >= 2)なのは覚えても良さそう。
    """

    if K >= 2**M:
        print(-1)
        return
    if M == 1 and K == 0:
        print("0 0 1 1")
        return
    if M == 1 and K == 1:
        print(-1)
        return

    b = [i for i in range(K)] + [i for i in range(K + 1, 2 ** M)]
    c = list(reversed(b))
    ans = b + [K] + c + [K]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
