def slove():
    import sys
    input = sys.stdin.readline
    a, b = list(map(int, input().rstrip('\n').split()))
    print(a if b >= a else a - 1)


if __name__ == '__main__':
    slove()
