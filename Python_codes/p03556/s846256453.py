def solve():
    N = int(input())
    for i in range(N, 0, -1):
        if (i ** 0.5).is_integer():
            print(i)
            exit()


if __name__ == "__main__":
    solve()