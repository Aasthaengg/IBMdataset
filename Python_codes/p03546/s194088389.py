H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]


# Warshall–Floyd
def main():
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    print(
        sum(
            c[a][1] for column in A for a in column if a >= 0 
        )
    )


if __name__ == "__main__":
    main()

