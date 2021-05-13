s = list(str(input()))
s.reverse()
S = []

c = ''
for i in range(len(s)):
    c += s[i]
    if S:
        if c != S[-1]:
            S.append(c)
            c = ''
    else:
        S.append(c)
        c = ''
#print(S)
print(len(S))
