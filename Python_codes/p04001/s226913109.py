S = list(input())
l = len(S)-1
su = 0
for i in range(2**l):
    q = S[0]
    for j in range(l):
        if (i>>j) & 1:
            q += '+' + S[j+1]
        else:q += S[j+1]
    su += eval(q)
print(su)