def slove():
    import sys
    input = sys.stdin.readline
    r = int(input().rstrip('\n'))
    g = int(input().rstrip('\n'))
    print(2 * g - r)


if __name__ == '__main__':
    slove()
