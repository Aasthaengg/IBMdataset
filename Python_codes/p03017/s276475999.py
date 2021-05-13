def main():
    n, a, b, c, d = list(map(lambda x: int(x) - 1, input().split()))
    n += 1
    s = list(input())
    s = s[a:max(c, d) + 1]
    for i in range(len(s) - 1):
        if s[i] == '#' and s[i + 1] == '#':
            print('No')
            exit()
    if c < d:
        print('Yes')
    else:
        ch = False
        for i in range(b, d + 1):
            if s[i - 1] == s[i] == s[i + 1] == '.':
                ch = True
        if ch:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
