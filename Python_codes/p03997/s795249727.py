def slove():
    import sys
    input = sys.stdin.readline
    a = int(input().rstrip('\n'))
    b = int(input().rstrip('\n'))
    h = int(input().rstrip('\n'))
    print((a + b) * h // 2)


if __name__ == '__main__':
    slove()
