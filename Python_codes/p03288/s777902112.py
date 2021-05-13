def slove():
    import sys
    input = sys.stdin.readline
    r = int(input().rstrip('\n'))
    if r < 1200:
        print("ABC")
    elif 1200 <= r < 2800:
        print("ARC")
    else:
        print("AGC")


if __name__ == '__main__':
    slove()
