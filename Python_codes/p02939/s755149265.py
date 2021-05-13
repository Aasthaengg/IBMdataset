
def main():
    S = input()
    cnt = 1
    bf = S[0]
    stmp = ''
    for i, s in enumerate(S):
        if i == 0:
            continue
        stmp += s
        if stmp == bf:
            continue
        cnt += 1
        bf = stmp
        stmp = ''

    print(cnt)

if __name__ == "__main__":
    main()
