def solve(string):
    n, i = map(int, string.split())
    return str(n - i + 1)


if __name__ == '__main__':
    print(solve(input()))
