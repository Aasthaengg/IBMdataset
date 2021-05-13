def solve():
    n = int(input())
    if 0 <= n < 10:
        print(n)
    elif 10 <= n < 100:
        print(9)
    elif 100 <= n < 1000:
        print(9 + n - 99)
    elif 1000 <= n < 10000:
        print(909)
    elif 10000 <= n < 100000:
        print(909 + n - 9999)
    else:
        print(90909)


if __name__ == '__main__':
    solve()
