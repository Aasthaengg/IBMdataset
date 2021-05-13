import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    p2idx = {x: i for i, x in enumerate(P)}

    # 数が連続する増加部分数列の最大の長さを調べる
    # ある数字pが右端となる時の部分数列の最大の長さを保持
    max_len = 1
    tmp = 1
    for p in range(2, N + 1):
        if p2idx[p] > p2idx[p - 1]:
            tmp += 1
            if max_len < tmp:
                max_len = tmp
        else:
            tmp = 1

    print(N - max_len)

if __name__ == "__main__":
    main()