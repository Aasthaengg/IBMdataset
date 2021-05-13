def slove():
    import sys
    input = sys.stdin.readline
    n, i = list(map(int, input().rstrip('\n').split()))
    print(n - i + 1)


if __name__ == '__main__':
    slove()
