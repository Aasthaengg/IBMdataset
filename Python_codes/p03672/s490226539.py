def resolve():
    S = input()
    for i in range(len(S)-1):
        S = S[:-1]
        if len(S)%2 == 0 and S[:len(S)//2] == S[len(S)//2:]:
            print(len(S))
            exit()
resolve()