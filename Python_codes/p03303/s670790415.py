def slove():
    import sys
    input = sys.stdin.readline
    s = list(str(input().rstrip('\n')))
    w = int(input().rstrip('\n'))
    print("".join(s[::w]))


if __name__ == '__main__':
    slove()
