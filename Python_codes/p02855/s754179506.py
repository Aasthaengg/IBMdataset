import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W, K = map(int, input().split())
    S = list(list(input()) for _ in range(H))
    ans = [[0] * W for _ in range(H)]

    count = 1
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans[i][j] = count
                count += 1

    for i in range(H):
        for j in range(1, W):
            if ans[i][j] == 0 and ans[i][j - 1]:
                ans[i][j] = ans[i][j - 1]

    for i in range(H):
        for j in range(W - 1)[::-1]:
            if ans[i][j] == 0 and ans[i][j + 1]:
                ans[i][j] = ans[i][j + 1]

    for i in range(1, H):
        for j in range(W):
            if ans[i][j] == 0 and ans[i - 1][j]:
                ans[i][j] = ans[i - 1][j]

    for i in range(H - 1)[::-1]:
        for j in range(W):
            if ans[i][j] == 0 and ans[i + 1][j]:
                ans[i][j] = ans[i + 1][j]

    for a in ans:
        print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
