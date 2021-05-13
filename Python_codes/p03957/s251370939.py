S = list(input())

C = []
F = []
for i, s in enumerate(S):
    if s == "C":
        C.append(i)
    elif s == "F":
        F.append(i)

if len(C) > 0 and len(F):
    if min(C) < max(F):
        print('Yes')
    else:
        print('No')
else:
    print('No')
