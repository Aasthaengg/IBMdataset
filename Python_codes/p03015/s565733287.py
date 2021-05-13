L = input()
dp1 = [0] * 100001 #Lを超えるか不明
dp2 = [0] * 100001 #Lを超えないことが確定
MOD = 10**9 + 7
dp1[0] = 1
for i,d in enumerate(L):
    if int(d) == 1:
        dp1[i+1] = dp1[i]*2 #(1,0) or (0,1)
        dp2[i+1] = dp1[i] + dp2[i]*3 #(0,0)で1から降格 
    if int(d) == 0:
        dp1[i+1] = dp1[i] #(0,0)
        dp2[i+1] = dp2[i]*3 #確定しているから、(0,0)(0,1)(1,0)何でも良い
    dp1[i+1] %= MOD    
    dp2[i+1] %= MOD    
N = len(L)
ans = dp1[N]+dp2[N]
print(ans%MOD)