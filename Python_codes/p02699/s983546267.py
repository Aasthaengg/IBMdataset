def solve(string):
    s, w = map(int, string.split())
    p = "" if s > w else "un"
    return p + "safe"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
