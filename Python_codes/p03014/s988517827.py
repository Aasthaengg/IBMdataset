import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    H, W = map(int, input().rstrip().split())
    G = []
    for i in range(H):
        s = list(input())
        G.append(s)
    # print(G)
    cnt = [[0 for j in range(W)] for i in range(H)]

    for i in range(H):
        done = [0] * W
        for j in range(W):
            if G[i][j] == "#":
                continue
            if done[j]:
                continue
            length = 0
            while j + length < W:
                if G[i][j+length] == "#":
                    break
                length += 1
            for k in range(length):
                cnt[i][j + k] += length
                done[j + k] = 1

    for j in range(W):
        done = [0] * H
        for i in range(H):
            if G[i][j] == "#":
                continue
            if done[i]:
                continue
            length = 0
            while i + length < H:
                if G[i+length][j] == "#":
                    break
                length += 1
            for k in range(length):
                cnt[i + k][j] += length
                done[i + k] = 1
    ans = 0
    for i in range(H):
        ans = max(ans, max(cnt[i]) - 1)
    print(ans)


if __name__ == "__main__":
    main()
