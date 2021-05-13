def slove():
    import sys
    input = sys.stdin.readline
    n ,m = list(map(int, input().rstrip('\n').split()))
    print((n - 1) * (m - 1))


if __name__ == '__main__':
    slove()
