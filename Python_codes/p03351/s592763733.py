def slove():
    import sys
    input = sys.stdin.readline
    a, b, c, d = list(map(int, input().rstrip('\n').split()))
    if abs(c- a) <= d:
        print("Yes")
    elif abs(a - b) <= d and abs(b - c) <= d:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    slove()
