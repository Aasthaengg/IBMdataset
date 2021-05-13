# AGC026A - Colorful Slimes 2
def main():
    n = int(input())
    A = tuple(map(int, input().rstrip().split()))
    ans, flg = 0, False
    for i, j in zip(A, A[1:]):
        if flg:
            flg = False
        else:
            if i == j:
                ans += 1
                flg = True
    print(ans)


if __name__ == "__main__":
    main()