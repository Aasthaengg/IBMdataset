def han(l):
    for i in range((len(l) // 2)):
        if l[i] != l[-i - 1]:
            return 0
    return 1

S = input()

f1 = han(S)
S2 = S[0:(len(S) // 2)]
S3 = S[len(S)//2 + 1 : len(S)]
f2 = han(S2)
f3 = han(S3)

if f1 * f2 * f3:
    print('Yes')
else:
    print('No')

