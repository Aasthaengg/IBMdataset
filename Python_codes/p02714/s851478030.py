def resolve():
    N = int(input())
    S = input()
    rem = 0
    for i in range(N):
        for j in range(i, N):
            k = 2*j - i
            if k < N and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                rem += 1
    print(S.count("R")*S.count("G")*S.count("B") - rem)


if '__main__' == __name__:
    resolve()
