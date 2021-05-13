def resolve():
    S = input()
    s = len(S) - 7
    if S == "keyence":
        print("YES")
    else:
        for i in range(len(S)-s-1):
            if S[:i+1]+S[i+s+1:] == "keyence":
                print("YES")
                exit()
        print("NO")
resolve()