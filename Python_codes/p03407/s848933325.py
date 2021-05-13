def solve(string):
    a, b, c = map(int, string.split())
    return "Yes" if a + b - c >= 0 else "No"


if __name__ == '__main__':
    print(solve(input()))
