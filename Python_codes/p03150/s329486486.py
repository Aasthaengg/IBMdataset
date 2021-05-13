def main():
    S = input()
    n = len(S)
    c = 0
    if S == 'keyence':
        print('YES')
        exit()
    for i in range(n):
        for j in range(i, n):
            s1 = S[:i] if i > 0 else ''
            s2 = S[j + 1:] if j + 1 < n else ''
            if s1 + s2 == 'keyence':
                print('YES')
                exit()
    print('NO')


if __name__ == '__main__':
    main()
