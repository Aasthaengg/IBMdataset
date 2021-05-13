N = int(input())

cntab = 0
cns = 0
cne = 0
cnse = 0
for _ in range(N):
    S = input()
    if S[0] == 'B' and S[-1] == 'A':
        cnse += 1
    elif S[0] == 'B':
        cns += 1
    elif S[-1] == 'A':
        cne += 1
    for s1, s2 in zip(S, S[1:]):
        if (s1 == 'A') and (s2 == 'B'):
            cntab += 1


if N == cnse:
    print(cntab + N - 1)
elif cnse == 0:
    print(cntab + min(cns, cne))
else:
    if (cns == 0) and (cne == 0):
        print(cntab + cnse - 1)
    elif (cns == 0) or (cne == 0):
        print(cntab + cnse)
    else:
        print(cntab + cnse + 1 + min(cns-1, cne-1))
