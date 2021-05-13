def slove():
    import sys
    input = sys.stdin.readline
    n, k = list(map(int, input().rstrip('\n').split()))
    print(n - k + 1)


if __name__ == '__main__':
    slove()
