import sys
def input(): return sys.stdin.readline().strip()

def main():
    W, H, N = map(int, input().split())
    mat = [[1] * W for _ in range(H)]
    for _ in range(N):
        x, y, a = map(int, input().split())
        if a == 1:
            for i in range(H):
                for j in range(x):
                    mat[i][j] = 0
        if a == 2:
            for i in range(H):
                for j in range(x, W):
                    mat[i][j] = 0
        if a == 3:
            for i in range(y):
                for j in range(W):
                    mat[i][j] = 0
        if a == 4:
            for i in range(y, H):
                for j in range(W):
                    mat[i][j] = 0
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += mat[i][j]
    print(ans)


if __name__ == "__main__":
    main()
