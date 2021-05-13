N = int(input())
C = [int(input())]
cindex = {C[0]: 0}
mod = 7 + 10 ** 9
counter = 0
for _ in range(N-1):
    c = int(input())
    if c != C[-1]:
        C.append(c)
        counter += 1
        if c not in cindex:
            cindex[c] = counter

DP = [[0, 1] for i in range(len(C))]
for i in range(1, len(C)):
    if cindex[C[i]] == i:
        DP[i][1] = DP[i-1][1]
    else:
        DP[i][0] = DP[cindex[C[i]]][1] 
        DP[i][1] = DP[i][0] + DP[i-1][1]
        DP[i][1] %= mod
        cindex[C[i]] = i
print(DP[-1][1])