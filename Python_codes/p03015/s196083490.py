l = input()

mod = 10**9+7


dplow = [0]*len(l)
dp2 = [0]*len(l)

dplow[0] = 1
dp2[0] = 2

for i in range(1,len(l)):
    dplow[i] += dplow[i-1]*3%mod
    if l[i] == "1":
        dplow[i] += dp2[i-1]%mod
        dp2[i] += dp2[i-1]*2%mod
    else:
        dp2[i] += dp2[i-1] %mod

print((dplow[-1]+dp2[-1])%mod)