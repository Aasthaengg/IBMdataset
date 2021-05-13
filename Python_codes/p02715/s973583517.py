N, K = map(int, input().split())
mod = 10**9 + 7

gcd = {}
s = 0

for x in range(K,0,-1):
  
    i = K // x
    tmp = pow(i,N,mod)  # 組み合わせ数
    
    if i > 1:
        for j in range(2,i+1):
            tmp -= gcd[j * x]
    
    gcd[x] = tmp
    s += (tmp * x) % mod
    s %= mod

print(s)