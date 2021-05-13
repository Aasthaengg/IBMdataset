def resolve():
    S = input()
    ans = []
    for i in range(len(S)-2):
        ans.append(abs(753-int(S[i]+S[i+1]+S[i+2])))
    print(min(ans))
resolve()