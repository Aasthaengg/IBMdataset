import string

S = input()
abc = string.ascii_lowercase

if len(S) == 26:
    for i in range(24, -1, -1):
        cand = list(S[i+1:])
        cand.sort()
        for c in cand:
            if ord(c) > ord(S[i]):
                print(S[:i]+c)
                exit(0)
    print(-1)
else:
    for l in abc:
        if l not in S:
            print(S+l)
            exit()
