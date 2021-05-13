
def resolve():
    H, W, A, B = map(int, input().split())
    G = [[0] * W for _ in range(H)]

    for i in range(B):
        for j in range(A):
            G[i][j] = 1

    for i in range(B, H):
        for j in range(A, W):
            G[i][j] = 1

    for g in G:
        print(*g, sep="")


if __name__ == "__main__":
    resolve()