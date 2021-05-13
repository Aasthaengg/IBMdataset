def solve():
    N = int(input())

    count_1 = 0
    for i in [_ for _ in range(1, N+1) if _ % 2 == 1]:
        count_2 = 0
        for j in range(1, i+1):
            if i % j == 0:
                count_2 += 1
        if count_2 == 8:
            count_1 += 1
    print(count_1)


if __name__ == "__main__":
    solve()