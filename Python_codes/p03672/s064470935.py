def resolve():
    S = input()
    for i in range(len(S) - 2, 0, -2):
        if S[0:i // 2] == S[i // 2:i]:
            print(i)
            return


resolve()
