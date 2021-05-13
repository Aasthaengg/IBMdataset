def main():
    S = input()
    ans = 1
    cp, cn = S[0], ''
    for c in S[1:]:
        cn = cn + c
        if cp != cn:
            ans += 1
            cp = cn
            cn = ''
    print(ans)


if __name__ == '__main__':
    main()
