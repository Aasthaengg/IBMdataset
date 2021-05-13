S = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

if len(S) == 26:
    if S == alpha[::-1]:
        print(-1)
        exit()
    for i in reversed(range(25)):
        for j in reversed(range(i, 26)):
            if S[i] < S[j]:
                print(S[:i] + S[j])
                exit()
else:
    for x in alpha:
        if x not in S:
            print(S + x)
            break
