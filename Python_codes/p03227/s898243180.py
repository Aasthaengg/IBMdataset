def slove():
    import sys
    input = sys.stdin.readline
    s = str(input().rstrip('\n'))
    if len(s) == 2:
        print(s)
    else:
        print(s[2] + s[1] + s[0])


if __name__ == '__main__':
    slove()
