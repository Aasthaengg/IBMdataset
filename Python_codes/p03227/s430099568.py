S = list(input())
s = ""
if len(S)==3:
    s = S[0]
    S[0] = S[2]
    S[2] = s
    print(''.join(map(str, S)))
else:
    print(''.join(map(str, S)))
