N = int(input())
S1 = input()
S2 = input()
ans = 1
mod = 1000000007
i = 0
while i < N:
    if i == 0:
        if S1[i] == S2[i]:
            ans *= 3
            i += 1
        else:
            ans *= 6
            i += 2
    else:
        if S1[i] == S2[i]:
            if S1[i-1] == S2[i-1]:
                ans *= 2
                ans %= mod
                i += 1
            else:
                ans *= 1
                ans %= mod
                i += 1
        else:
            if S1[i-1] == S2[i-1]:
                ans *= 2
                ans %= mod
                i += 2
            else:
                ans *= 3
                ans %= mod
                i += 2
print(ans)