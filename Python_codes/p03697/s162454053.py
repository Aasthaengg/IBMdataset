def slove():
    import sys
    input = sys.stdin.readline
    a, b = list(map(int, input().rstrip('\n').split()))
    print(a + b if a + b < 10 else "error")


if __name__ == '__main__':
    slove()
