import sys
from collections import defaultdict
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    """
    ６のべき乗しか引き出せない部分問題を考える。
    このとき最適な支払方法は、当然大きい金額を序盤に一気に下ろすこと。
    なのでN円をi円と(N - i)円に分けて片方を6のべき、もう片方を９のべきで支払って
    その合計を見ればよい。

    それぞれの支払い方はすなわち６進数（９進数）展開することに他ならないので
    １円から支払う方法を考えた方が早い。
    """
    N = int(input())
    ans = N
    for i in range(N + 1):
        cnt = 0
        t = i
        while t > 0:
            cnt += t % 6
            t //= 6
        t = N - i
        while t > 0:
            cnt += t % 9
            t //= 9
        ans = min(ans, cnt)
    print(ans)


if __name__ == "__main__":
    main()
