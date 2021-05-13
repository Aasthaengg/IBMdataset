S = input()
T = input()

d = {}

for i in range(len(S)):
    #print(S[i],"to",T[i])
    if S[i] not in d:
        if T[i] in d.values():
            print('No')
            break
        else:
            d[S[i]] = T[i]
    else:
        if d[S[i]] != T[i]:
            print('No')
            break
    #print(d)
else:
    print('Yes')