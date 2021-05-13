K = int(input())
S = list(input())
S2 = []

if len(S) <= K:
    print(''.join(S))
else:
    for i in range(K):
        n = S[i]
        S2.append(n)
if len(S2) == K:
    print(''.join(S2) + '...')