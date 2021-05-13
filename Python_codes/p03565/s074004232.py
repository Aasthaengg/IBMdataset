S = input().strip()
T = input().strip()

listS = list(S)
f = False
for i in range(len(S) - len(T), -1, -1):
    for ji, j in enumerate(range(i, i + len(T))):
        if S[j] == T[ji] or S[j] == "?":
            continue
        else:
            break
    else:
        for ji, j in enumerate(range(i, i + len(T))):
            listS[j] = T[ji]
        f = True
        break

if f:
    for i in range(len(S)):
        if listS[i] == "?":
            listS[i] = 'a'

    print("".join(listS))
else:
    print("UNRESTORABLE")