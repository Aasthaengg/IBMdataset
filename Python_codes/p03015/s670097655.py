L = input()
n = len(L)
mod = 10**9+7
pow3 = [1]
for i in range(1,n):
    x = (3*pow3[i-1])%mod
    pow3.append(x)
ans = 0
for i in range(1,n+1):
    if L[-i] == '1':
        if i == 1:
            ans = 3
        else:
            ans = ans*2 % mod
            ans = (ans + pow3[i-1])%mod
    else:
        if i == 1:
            ans = 1
print(ans)