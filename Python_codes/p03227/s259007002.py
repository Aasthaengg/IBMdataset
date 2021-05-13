def slove():
    import sys
    input = sys.stdin.readline
    s = str(input().rstrip('\n'))
    if len(s) == 2:
        print(s)
    else:
        print("".join([s[i] for i in range(len(s)-1, -1, -1)]))


if __name__ == '__main__':
    slove()
