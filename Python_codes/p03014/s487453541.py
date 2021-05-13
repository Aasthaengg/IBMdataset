import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def main():
    H, W = map(int, input().split())
    S = [[] for _ in range(H)]
    count = [[0] * W for _ in range(H)]

    # read and horizontal
    for i in range(H):
        s = list(input())
        S[i] = s
        con = 0
        for j in range(W):
            if s[j] == "#":
                con = 0
                continue
            elif con == 0:
                con = 1
                k = j + 1
                while k < W:
                    if s[k] == ".":
                        con += 1
                        k += 1
                    else:
                        break
                count[i][j] = con
            elif con > 0:
                count[i][j] = con

    pass
    # vertical
    for j in range(W):
        ##############
        con = 0
        for i in range(H):
            if S[i][j] == "#":
                con = 0
                continue
            elif con == 0:
                con = 1
                k = i + 1
                while k < H:
                    if S[k][j] == ".":
                        con += 1
                        k += 1
                    else:
                        break
                count[i][j] += con
            elif con > 0:
                count[i][j] += con

    m = 0
    for i in range(H):
        m =max(m,max(count[i]))
    print(m-1)

if __name__ == "__main__":
    main()
