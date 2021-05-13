N, K = map(int, input().split())
S = input()
L = []
R = []
maximum = 0
if S[0] == "0":
    L.append(0)
if S[N-1] == "0":
    R.append(N-1)
for n in range(N-1):
    if S[n] == "1" and S[n+1] == "0":
        L.append(n+1)
    if S[-n-1] == "1" and S[-n-2] == "0":
        R.append(N-n-2)
L.append(N)
R.append(-1)
R.reverse()
if len(L) <= K:
    print(N)
else:
    for n in range(len(L)-K):
        maximum = max(maximum, L[n+K]-R[n]-1)
    print(maximum)