# AGC026A - Colorful Slimes 2
def main():
    N, *A = map(int, open(0).read().split())
    ans, flg = 0, 0  # flg: change j (i in next pair) or not
    for i, j in zip(A, A[1:]):
        if flg:
            flg ^= 1
        else:
            if i == j:
                ans += 1
                flg ^= 1
    print(ans)


if __name__ == "__main__":
    main()