def slove():
    import sys
    input = sys.stdin.readline
    n, a, b = list(map(int, input().rstrip('\n').split()))
    print(min(a, b), max(0, a + b - n))


if __name__ == '__main__':
    slove()
