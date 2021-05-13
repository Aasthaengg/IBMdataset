def slove():
    import sys
    input = sys.stdin.readline
    n, k = list(map(int, input().rstrip('\n').split()))
    if k == 1:
        print(0)
    else:
        print(n - k)


if __name__ == '__main__':
    slove()
