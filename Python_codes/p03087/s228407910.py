N, Q, S, *_LR = open(0).read().split()
N = int(N)
Q = int(Q)
LR = list(zip(*[map(int, iter(_LR))]*2))

AC = [0]*(N)

for i in range(1, N):
    if S[i-1] == "A":
        if S[i] == "C":
            is_AC = 1
        else:
            is_AC = 0
    else:
        is_AC = 0

    if i == 1:
        AC[i] = is_AC
    else:
        AC[i] = AC[i-1] + is_AC
        
for L,R in LR:
    print(AC[R-1] - AC[L-1])