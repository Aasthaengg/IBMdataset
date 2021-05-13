def slove():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = int(input().rstrip('\n'))
    print(n * n - a)


if __name__ == '__main__':
    slove()
