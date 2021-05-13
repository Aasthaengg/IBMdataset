import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())

    M = (N - 1) * (N - 2) // 2
    if K > M:
        print(-1)
        return

    ans = []
    for i in range(1, N):
        ans.append((i, N))

    cnt = 0
    for i in range(1, N):
        done = False
        for j in range(i + 1, N):
            if cnt == M - K:
                done = True
                break
            ans.append((i, j))
            cnt += 1
        if done:
            break

    print(len(ans))
    for i, j in ans:
        print(i, j)

    return


if __name__ == '__main__':
    main()
