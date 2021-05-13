def slove():
    import sys
    input = sys.stdin.readline
    ls = list("CODEFESTIVAL2016")
    s = str(input().rstrip('\n'))
    cnt = 0
    for i in range(len(s)):
        if ls[i] != s[i]:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    slove()
