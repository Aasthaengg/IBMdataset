def slove():
    import sys
    input = sys.stdin.readline
    n, k = list(map(int, input().rstrip('\n').split()))
    if n % k == 0:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    slove()
