import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    d_0 = [N for _ in range(61)]
    d_1 = [0 for _ in range(61)]
    max_d = 0
    for a in A:
        d = 0
        while a > 0:
            keta = a % 2
            a //= 2
            if keta == 1:
                d_0[d] -= 1
                d_1[d] += 1
            d += 1
        if d > max_d:
            max_d = d
    # print(d_0)
    # print(d_1)
    answer = 0
    for i in range(max_d):
        answer += d_0[i] * d_1[i] * 2 ** i
        answer %= MOD
    print(answer)


if __name__ == "__main__":
    main()
