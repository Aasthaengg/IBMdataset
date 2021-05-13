def main():
    S = input()

    N = len(S)
    ans = 1

    i = 1
    chars = ''
    buf = S[0]
    while i < N:
        chars += S[i]
        if buf == chars:
            pass
        else:
            ans += 1
            buf = chars
            chars = ''
        i += 1
    print(ans)
main()