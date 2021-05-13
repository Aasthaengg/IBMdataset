def slove():
    import sys
    input = sys.stdin.readline
    a, b, c, d = list(map(int, input().rstrip('\n').split()))
    ab = a + b
    cd = c + d
    if ab > cd:
        print("Left")
    elif ab < cd:
        print("Right")
    else:
        print("Balanced")


if __name__ == '__main__':
    slove()
