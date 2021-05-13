def slove():
    import sys
    input = sys.stdin.readline
    n, a, b = list(map(int, input().rstrip('\n').split()))
    print(min(n * a, b))


if __name__ == '__main__':
    slove()
