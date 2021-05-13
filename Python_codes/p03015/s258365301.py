MOD = 10**9+7
L = input()

DP1 = [0]
DP2 = [1]

for i in L:
    if i == '1':
        x = (DP1[-1]*3+DP2[-1])%MOD
        y = (DP2[-1]*2)%MOD
        DP1.append(x)
        DP2.append(y)
    else:
        x = (DP1[-1]*3)%MOD
        DP1.append(x)
print((DP1[-1]+DP2[-1])%MOD)
