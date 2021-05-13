import sys

def solve():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    S = tuple(tuple(input().strip("\n")) for _ in range(H))
    A = [[-1 for _ in range(W)] for i in range(H)]
    startR = 0
    line = 0
    endR = 0
    cakeN = 1
    for i in range(H):
        if "#" in S[i]:
            line = i
            endR = i + 1
            break
    while endR < H:
        if "#" in S[endR]: #切り分けの処理。列方向に走査
            startC = 0
            for j in range(W):
                if S[line][j] == "#":
                    endC = j + 1
                    break
            while endC < W:
                if S[line][endC] == "#":
                    for si in range(startR, endR):
                        for sj in range(startC, endC): A[si][sj] = cakeN
                    startC = endC
                    cakeN += 1
                endC += 1
            for si in range(startR, endR):
                for sj in range(startC, endC):
                    A[si][sj] = cakeN
            cakeN += 1
            startR = line = endR

        endR += 1

    startC = 0
    for j in range(W):
        if S[line][j] == "#":
            endC = j + 1
            break
    while endC < W:
        if S[line][endC] == "#":
            for si in range(startR, endR):
                for sj in range(startC, endC):
                    A[si][sj] = cakeN
            startC = endC
            cakeN += 1
        endC += 1
    for si in range(startR, endR):
        for sj in range(startC, endC):
            A[si][sj] = cakeN

    for i, a in enumerate(A): print(" ".join(map(str, a)))

    return 0

if __name__ == "__main__":
    solve()