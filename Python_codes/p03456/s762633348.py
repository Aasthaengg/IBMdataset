def solve():
    n = int(input().replace(' ', ''))
    if (n ** 0.5).is_integer():
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()
