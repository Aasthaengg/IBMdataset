import sys


def input():
    return sys.stdin.readline().strip()


MOD = 998244353


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    height = [[0] * W for _ in range(H)]
    width = [[0] * W for _ in range(H)]

    for h in range(H):
        cnt = 0
        for w in range(W):
            if S[h][w] == ".":
                cnt += 1
            else:
                width[h][w - cnt : w] = [cnt] * cnt
                cnt = 0
        width[h][W - cnt : W] = [cnt] * cnt
    for w in range(W):
        cnt = 0
        for h in range(H):
            if S[h][w] == ".":
                cnt += 1
            else:
                for i in range(cnt):
                    height[h - cnt + i][w] = cnt
                cnt = 0
        for i in range(cnt):
            height[H - cnt + i][w] = cnt
    answer = 0
    for h in range(H):
        for w in range(W):
            ans = width[h][w] + height[h][w] - 1
            if ans > answer:
                answer = ans
    print(answer)


if __name__ == "__main__":
    main()
