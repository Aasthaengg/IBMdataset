S = input()
if S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()
import string
if len(S) < 26:
    tmp = sorted(list(set(list(string.ascii_lowercase))-set(list(S))))
    print(S+tmp[0])
    exit()
for i in range(26,-1,-1):
    tmp1 = S[:i]
    tmp2 = sorted(list(S[i:]))
    for t in tmp2:
        if S < tmp1+t:
            print(tmp1+t)
            exit()