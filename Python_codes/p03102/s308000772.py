def main():
    n, m, c = map(int, input().split())
    b_list = list(map(int, input().split()))
    a_list = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        tmp_sum = 0
        for j in range(m):
            tmp_sum += a_list[i][j] * b_list[j]
        if tmp_sum + c > 0:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
