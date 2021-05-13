l = input()
MOD = 10**9 + 7
dp1 = [0]*(len(l)+1)#l以下が確定してる
dp2 = [0]*(len(l)+1)#l以下が確定してない
num = l.count("1")
dp1[0]=1
dp2[0]=0
for i in range(1,len(l)+1):
    if(l[i-1]=="1"):
        dp1[i] = 2*dp1[i-1]%MOD
        dp2[i] = ((3*dp2[i-1])+dp1[i-1])%MOD
    else:
        dp1[i] = dp1[i-1]%MOD
        dp2[i] = 3*dp2[i-1]%MOD
print((dp1[-1]+dp2[-1])%MOD)
