def slove():
    import sys
    input = sys.stdin.readline
    x = int(input().rstrip('\n'))
    print("ABC" if x < 1200 else "ARC")


if __name__ == '__main__':
    slove()
