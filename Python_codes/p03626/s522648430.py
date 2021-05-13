MOD = 1000000007
N = int(input())
S1 = input()
S2 = input()
if S1[0] == S2[0]:
    ans = 3
    p = 1
    i = 1
else:
    ans = 6
    p = 0
    i = 2

while i < N:
    if S1[i] == S2[i]:
        if p:
            ans *= 2
        p = 1
        i += 1
    else:
        if p:
            ans *= 2
        else:
            ans *= 3
        p = 0
        i += 2
    ans %= MOD
print(ans)
