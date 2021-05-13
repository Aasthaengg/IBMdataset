n = int(input())
mod = 10**9+7

def prime_decomposition(n):
    i = 2
    tank = []
    while i * i <= n:
        while n%i == 0:
            n /= i
            tank.append(i)
        i += 1
    if n > 1:
        tank.append(int(n))
    return tank

dic = {i:0 for i in range(n+1)}
for i in range(2, n+1):
    l = prime_decomposition(i)
    for x in l:
        dic[x] += 1
ans = 1
for k,v in dic.items():
    if v!=0:
        ans *= (v+1)
        ans %= mod
print(ans%mod)