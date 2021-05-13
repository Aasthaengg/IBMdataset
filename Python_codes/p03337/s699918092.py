def slove():
    import sys
    input = sys.stdin.readline
    a, b = list(map(int, input().rstrip('\n').split()))
    print(max(a + b, a - b, a * b))


if __name__ == '__main__':
    slove()
