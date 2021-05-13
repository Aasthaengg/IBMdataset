def slove():
    import sys
    input = sys.stdin.readline
    s = str(input().rstrip('\n'))
    w = int(input().rstrip('\n'))
    print(s[::w])


if __name__ == '__main__':
    slove()
