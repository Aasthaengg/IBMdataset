def slove():
    import sys
    input = sys.stdin.readline
    a, b, c = list(map(int, input().rstrip('\n').split()))
    print("Yes" if a == b == c else "No")


if __name__ == '__main__':
    slove()
