import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    K = (1 + (8 * N + 1) ** 0.5) / 2
    if not K.is_integer():
        print('No')
        return
    K = int(K)

    ans = [[] for _ in range(K)]
    num = 1
    for k in range(K):
        for l in range(k + 1, K):
            ans[k].append(num)
            ans[l].append(num)
            num += 1
    print('Yes')
    print(K)
    for row in ans:
        print(K - 1, *row)


if __name__ == '__main__':
    main()
