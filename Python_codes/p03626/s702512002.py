N = int(input())
S1 = input()
S2 = input()
S = [S1,S2]
mod = 10**9+7
ans = 1
i = 0
prev = None
while i < N:
    if S[0][i] == S[1][i]:
        i += 1
        if prev is None:
            ans *= 3
        elif prev:
            ans *= 2
        else:
            ans *= 1
        prev = True
    else:
        i += 2
        if prev is None:
            ans *= 6
        elif prev:
            ans *= 2
        else:
            ans *= 3
        prev = False
    ans %= mod
print(ans%mod)