import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    ok = 10 ** 3
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if N <= mid * (mid - 1) // 2:
            ok = mid
        else:
            ng = mid
    K = ok
    if not N == K * (K - 1) // 2:
        print('No')
        return

    num = 1
    ans = [[0] * (K - 1) for _ in range(K - 1)]
    for i in range(K - 1):
        for j in range(i + 1):
            ans[i][j] = ans[j][i] = num
            num += 1

    ans.append([ans[i][i] for i in range(K - 1)])
    ans = ["{} {}".format(K - 1, ' '.join(map(str, row))) for row in ans]

    print('Yes')
    print(K)
    print('\n'.join(ans))


if __name__ == '__main__':
    main()
