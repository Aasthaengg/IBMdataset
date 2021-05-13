def solve(string):
    n, x, t = map(int, string.split())
    return str((n + x - 1) // x * t)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
