def main():
    n, m, c = map(int, input().split())
    b_lst = list(map(int, input().split()))
    a_lst = [0] * n
    for i in range(n):
        a_lst[i] = list(map(int, input().split()))

    count = 0
    for i in range(n):
        ab = 0
        for j in range(m):
            ab += a_lst[i][j] * b_lst[j]
        abc = ab + c

        if abc > 0:
            count += 1

    print(count)


if __name__ == '__main__':
    main()