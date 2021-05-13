S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
if len(S) < 26:
    for char in alp:
        if not char in S:
            print(S+char)
            exit()
else:
    for i in range(1,26)[::-1]:
        if S[i-1] < S[i]:
            for j in range(i,26)[::-1]:
                if S[j] > S[i-1]:
                    print(S[:i-1]+S[j])
                    exit()
    print(-1)