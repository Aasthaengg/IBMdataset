import sys

def solve():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    S = [list(input().strip("\n")) for _ in range(H)]
    round = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                count = 0
                for dh, dw in round:
                    if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw] == "#":
                        count += 1
                S[h][w] = str(count)
    for h in range(H): print("".join(S[h]))

    return 0

if __name__ == "__main__":
    solve()