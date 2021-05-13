N, K, C = map(int, input().split())
S = input()

L = []
lenL = 0
R = []
lenR = 0

c = 0
for i in range(N):
    if S[i] == 'o' and c <= 0:
        L.append(i + 1)
        lenL += 1
        if lenL == K:
            break
        c = C
    else:
        c -= 1

c = 0
for i in list(range(N))[::-1]:
    if S[i] == 'o' and c <= 0:
        R.append(i + 1)
        lenR += 1
        if lenR == K:
            break
        c = C
    else:
        c -= 1

for i in range(K):
    if L[i] == R[K - i - 1]:
        print(L[i])
