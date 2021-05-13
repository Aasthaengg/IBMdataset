import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
mod = 10**9 + 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = []
    for i, a in enumerate(A):
        B.append((a, i + 1))
    B.sort()
    #print(B)

    """
    活発度が大きい方から左右どちらかの端に移動させるが左右どちらになるかは一般に不明。
    しかし端から埋まるのは明らか（厳密な論証はmaspyさんの解説がわかりやすい）なので、
    ここから先をDPすればよい。具体的には
        dp[n][L] = (n人並べているとして左にL人いるときのうれしさの最大値)
    とすれば、これよりdp[n+1][L], dp[n+1][L+1]が更新できる。
    またn人の部分はdpとdp2間の遷移にしてメモリ削減。
    """

    dp = [0] * (N + 1)
    for n in range(1, N + 1):
        (a, i) = B.pop()
        dp2 = [0] * (N + 1)
        dp2[0] = dp[0] + a * abs((N - n + 1) - i)
        for l in range(1, n): # 1-indexedなことに注意
            dp2[l] = max(dp[l - 1] + a * abs(i - l), dp[l] + a * abs((N - n + l + 1) - i))
        dp2[n] = dp[n - 1] + a * abs(n - i)
        dp = dp2
        #print("{}人配置→dp={}".format(n, dp))
    print(max(dp))


if __name__ == "__main__":
    main()
