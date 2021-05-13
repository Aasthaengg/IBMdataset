S = input()
T = input()

if len(S) < len(T):
    print("UNRESTORABLE")
else:
    for i in reversed(range(len(S)-len(T)+1)):
        flg = True
        for j in range(len(T)):
            if S[i+j] != "?":
                if S[i+j] != T[j]:
                    flg = False
        if flg:
            list_s = list(S)
            for j in range(len(T)):
                list_s[i+j] = T[j]

            for j in range(len(list_s)):
                if list_s[j] == "?":
                    list_s[j] = "a"
            print(*list_s, sep="")
            exit()

    print("UNRESTORABLE")