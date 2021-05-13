def main():
    S = [s for s in input()]
    As = 0
    BCs = 0
    N = len(S)
    i = 0
    ans = 0
    while i < N - 1:
        s0, s1 = S[i], S[i + 1]
        if s0 == 'A':
            As += 1
            i += 1
            continue
        if s0 != 'B' or s1 != 'C':
            As = 0
            i += 1
            continue
        BCs = 1
        i += 2
        while i < N - 1:
            s0, s1 = S[i], S[i + 1]
            if s0 != 'B' or s1 != 'C':
                break
            BCs += 1
            i += 2
        ans += As * BCs
    print(ans)

if __name__ == '__main__':
    main()
