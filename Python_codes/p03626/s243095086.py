N = int(input())
S = [input() for _ in range(2)]

MOD = 1000000007
i = 0
C = []
while i < N:
    if S[0][i] == S[1][i]:
        C.append(0)
        i += 1
    else:
        C.append(1)
        i += 2

ans = 3 if C[0] == 0 else 6
for i in range(len(C) - 1):
    if C[i] == 0:
        ans = ans * 2 % MOD
    elif C[i + 1] == 1:
        ans = ans * 3 % MOD
print(ans)
