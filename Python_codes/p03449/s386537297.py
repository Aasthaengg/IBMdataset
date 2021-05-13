def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    lst = [[0 for _ in range(N)] for _ in range(2)]
    lst[0][0] = A[0][0]
    lst[1][0] = A[0][0] + A[1][0]

    for i in range(1, N):
        lst[0][i] = lst[0][i - 1] + A[0][i]

    for i in range(1, N):
        lst[1][i] = max(lst[0][i], lst[1][i - 1]) + A[1][i]

    print(lst[1][N - 1])


if __name__ == "__main__":
    main()
