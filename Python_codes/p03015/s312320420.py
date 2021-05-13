L = input()
mod = 10**9 + 7

x = len(L)
L = int(L, 2)
DP1 = [0] * (x+1)  # sure under L
DP2 = [0] * (x+1)  # possible under L
DP1[1] = 1
DP2[1] = 2
for i in range(2, x+1):
    if (L >> (x-i)) & 1:
        DP1[i] = (DP1[i-1] * 3 + DP2[i-1]) % mod
        DP2[i] = DP2[i-1] * 2 % mod

    else:
        DP1[i] = DP1[i-1] * 3 % mod
        DP2[i] = DP2[i-1]
ans = (DP1[x] + DP2[x]) % mod
print(ans)