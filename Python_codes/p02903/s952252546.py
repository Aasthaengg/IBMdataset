import sys

def solve():
    input = sys.stdin.readline
    H, W, A, B = map(int, input().split())
    S = [[None] * W for _ in range(H)]
    for h in range(B):
        for w in range(A): S[h][w] = 0
        for w in range(A, W): S[h][w] = 1
    for h in range(B, H):
        for w in range(A): S[h][w] = 1
        for w in range(A, W): S[h][w] = 0
    for h in range(H):
        print("".join(map(str, S[h])))

    return 0

if __name__ == "__main__":
    solve()