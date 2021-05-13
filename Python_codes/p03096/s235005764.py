import sys

MOD = 10**9 + 7

N = int(input())
Cs = [int(sys.stdin.readline())-1 for _ in range(N)]

numCs = [0] * (2 * 10**5)
anss = [0] * N
numCs[Cs[0]] = 1
anss[0] = 1
for i, C in enumerate(Cs[1:], 1):
    if C == Cs[i-1]:
        anss[i] = anss[i-1]
    else:
        numCs[C] += anss[i-1]
        anss[i] = numCs[C] % MOD

print(anss[-1])
