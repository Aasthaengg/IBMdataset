def main():
    ans = 0
    S = input()
    N = len(S)
    ans = 0
    now = 0
    skip = -1
    for i, s in enumerate(S):
        if i <= skip:
            continue
        if s == "A" and S[i+1:i+3] == "BC":
            now += 1
            ans += now
            skip = i+2
        elif s == "A":
            now += 1
        elif s == "B" and i < N-1 and S[i+1] == "C":
            ans += now
            skip = i+1
        else:
            now = 0
    print(ans)


if __name__ == '__main__':
    main()
