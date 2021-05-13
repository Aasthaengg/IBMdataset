def main():

    S = input()
    ref = S[0]
    i = 1
    ans = 1
    while i < len(S):
        if S[i] == ref:
            if i < len(S)-1:
                ref = S[i:i+2]
                ans += 1
                i += 2
            else:
                i += 1
        else:
            ref = S[i]
            ans += 1
            i += 1
    return ans


if __name__ == '__main__':
    print(main())
