def slove():
    import sys
    input = sys.stdin.readline
    a, b = list(map(int, input().rstrip('\n').split()))
    print(a + b if b % a == 0 else b - a)


if __name__ == '__main__':
    slove()
