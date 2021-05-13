def main():
    S = input()
    K = int(input())

    def cut(s):
        for c in s:
            yield c
            if c != '1': break

    *s, = cut(S)
    if len(s) < K:
        print(s[-1])
    else:
        print(s[K - 1])


if __name__ == '__main__':
    main()
