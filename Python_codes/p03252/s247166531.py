S1 = input()
S2 = input()

ss1 = {}
ss2 = {}
N = len(S1)
for i in range(N):
    if S1[i] not in ss1.keys():
        ss1[S1[i]] = S2[i]
    elif ss1[S1[i]] != S2[i]:
        print('No')
        exit(0)
    if S2[i] not in ss2.keys():
        ss2[S2[i]] = S1[i]
    elif ss2[S2[i]] != S1[i]:
        print('No')
        exit(0)

print('Yes')
