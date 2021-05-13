def slove():
    import sys
    input = sys.stdin.readline
    t, x = list(map(int, input().rstrip('\n').split()))
    print(t / x)


if __name__ == '__main__':
    slove()
