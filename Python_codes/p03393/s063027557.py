S = input()
s_set = set(S)
ind = len(S)

if len(S) == 26:
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        exit()
    for i in range(24, -1, -1):
        if ord(S[i]) <= ord(S[i+1]):
            ind = i
            break
    ans = S[:ind]
    for s in reversed(S[ind+1:]):
        if ord(s) > ord(S[ind]):
            print(ans + s)
            exit()

else:        
    for i in range(26):
        if chr(i+97) in s_set:
            continue
        else:
            print(S + chr(i+97))
            break