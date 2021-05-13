def slove():
    import sys
    input = sys.stdin.readline
    x, t = list(map(int, input().rstrip('\n').split()))
    print(max(x - t, 0))


if __name__ == '__main__':
    slove()
