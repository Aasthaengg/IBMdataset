def solve(string):
    n, a, b = map(int, string.split())
    return str(min(n * a, b))


if __name__ == '__main__':
    print(solve(input()))
