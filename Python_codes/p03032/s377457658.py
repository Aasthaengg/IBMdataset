import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0

    for i in range(min(N + 1, K+1)):  # 左から i 個取る　　
        for j in range(min(N + 1 - i, K - i+1)):  # 右からi個取る 計算量10^3
            res = K - i - j  # 残り行動回数
            agg = V[:i] + V[N  - j:]
            agg.sort(reverse=True)
            while res > 0 and agg:
                if agg[-1] < 0:
                    agg.pop()
                    res -= 1
                else:
                    break
            ans = max(sum(agg), ans)
    print(ans)


if __name__ == "__main__":
    main()
