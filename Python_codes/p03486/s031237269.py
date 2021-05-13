def main():
    s = input()
    t = input()

    s = sorted(s)
    t = sorted(t)[::-1]

    N = len(s)
    M = len(t)

    if N < M:
        if s == t[:N]:
            print('Yes')
            return
    N = min(N, M)
    i = 0
    while i < N and s[i] == t[i]:
        i += 1
    if i < N and s[i] < t[i]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
