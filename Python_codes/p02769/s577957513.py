n, k = list(map(int, input().split()))

mod = 10**9 + 7
k = min(k, n-1)

def choose(n, r):
    x = 1
    y = 1
    for i in range(1, r+1):
        x = (x * (n-i+1)) % mod
        y = (y * i) % mod
    return (x * pow(y, mod-2, mod)) % mod

kaijo = [1]
for i in range(1,n+1): 
  kaijo.append(kaijo[i-1]*i % mod)

ans = 0
for i in range(k+1):
#    ans += (choose(n, min(i,n-i)) * choose(n-1, min(i,n-1-i))) % mod
    ans += (kaijo[n] * pow(kaijo[i]*kaijo[n-i], mod-2,mod) % mod) * (kaijo[n-1]*pow(kaijo[i]*kaijo[n-1-i],mod-2,mod) % mod)
    ans = ans % mod
print(ans % mod)
