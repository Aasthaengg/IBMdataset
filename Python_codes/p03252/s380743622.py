# C - String Transformation

S = list(str(input()))
T = list(str(input()))
l = len(S)
d = set()

ans = 'Yes'
for i in range(l):
    if S[i] != T[i]:
        tmp = S[i]
        if S[i] in d or T[i] in d:
            ans = 'No'
            break
        d.add(T[i])
        for j in range(i, l):
            if S[j] == tmp:
                S[j] = T[i]
            elif S[j] == T[i]:
                S[j] = tmp
    else:
        d.add(T[i])

print(ans)