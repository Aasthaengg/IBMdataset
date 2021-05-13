def slove():
    import sys
    input = sys.stdin.readline
    a, b = list(map(int, input().rstrip('\n').split()))
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)


if __name__ == '__main__':
    slove()
