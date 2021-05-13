import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    N, C = map(int, input().split())
    sushi = []
    for _ in range(N):
        x, v = map(int, input().split())
        sushi.append((x, v))

    """
    まず最初の観察として、行ったり来たりしながら寿司をゲットするのは非効率。
    なので移動範囲は開始位置を含む円弧になる。
    円弧の左端をA、右端をB、開始位置をOとすると、移動方法は
        OA -> AB もしくはOB -> BA
    の２通り考えられる。

    それぞれに対してはOからの得点の累積和を前計算しておけばO(N^2)で答えが求まる。
    さらに次の工夫をすることでO(N)で計算が可能になる。

    OA->ABの場合で考える。まずBの位置を一箇所固定する。
    この時最適なAの位置をO(1)で取得できれば良いので、あらかじめ
        [v1　-　x1 * 2, v1 + v2 - x2 * 2, v1 + v2 + v3 - x3 * 2, ... ]
    の中の最大値を計算しておけば良い。
    あとはこれに(vN + v(N-1) + ... + vB) - (C - xB)を加えたものが得点になる。
    """

    #累積和の前計算
    A_sum = [0] # = [0, v1, v1 + v2, v1 + v2 + v3, ... ]
    B_sum = [0] # = [0, vN, vN + v(N - 1), vN + v(N - 1) + v(N - 2), ... ]
    A_max = [(0, 0)] # A_max[i] = (i番目の寿司まで見た時に一番得点が大きい場所とその得点の組)
    B_max = [(0, 0)] # B_max[i] = (N-i番目の寿司まで見た時に一番得点が大きい場所とその得点の組)
    for x, v in sushi:
        A_sum.append(A_sum[-1] + v)
        cand = A_sum[-1] - x * 2
        A_max.append(max(A_max[-1], (cand, x)))
    for x, v in sushi[::-1]:
        B_sum.append(B_sum[-1] + v)
        cand = B_sum[-1] - (C - x) * 2
        B_max.append(max(B_max[-1], (cand, x)))
    #print("A_sum={}".format(A_sum))
    #print("B_sum={}".format(B_sum))
    #print("A_max={}".format(A_max))
    #print("B_max={}".format(B_max))

    # OA->ABの場合の最大得点
    ans1 = -10**10
    for b in range(N, 0, -1):
        val = B_sum[N-b+1] - (C - sushi[b - 1][0])
        #print("b={} -> val={}".format(b, val))
        ans1 = max(ans1, A_max[b - 1][0] + val)

    # OB->BAの場合の最大得点
    ans2 = -10**10
    for a in range(1, N + 1):
        val = A_sum[a] - sushi[a - 1][0]
        #print("a={} -> val={}".format(a, val))
        ans2 = max(ans2, B_max[N - a][0] + val)

    print(max(0, ans1, ans2))


if __name__ == "__main__":
    main()
