S = input()
T = input()

dcs = {}
dct = {}
for i, s in enumerate(S):
    if s in dcs and dcs[s] != T[i]:
        print("No")
        exit()
    else:
        dcs[s] = T[i]
else:
    for j, t in enumerate(T):
        if t in dct and dct[t] != S[j]:
            print("No")
            exit()
        else:
            dct[t] = S[j]
    else:
        print("Yes")