# D - Coloring Dominoes

N = int(input())
S1 = input()
S2 = input()
MOD = 10**9 + 7

if S1[0] == S2[0]:
    same_domino = False
    ans = 3
else:
    same_domino = True
    ans = 3*2

for i in range(1, N):
    if S1[i] == S2[i] and S1[i-1] == S2[i-1]:
        ans *= 2
    elif S1[i] == S2[i] and S1[i-1] != S2[i-1]:
        pass
    elif S1[i] != S2[i] and same_domino:
        same_domino = False
    elif S1[i] != S2[i] and not same_domino and S1[i-1] == S2[i-1]:
        ans *= 2
        same_domino = True
    elif S1[i] != S2[i] and not same_domino and S1[i-1] != S2[i-1]:
        ans *= 3
        same_domino = True

print(ans % MOD)