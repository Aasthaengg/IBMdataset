k = int(input())
s = input()
mod = 10**9 + 7

n = 2*10**6 + 1
factorial = [1]
inverse = [1]
pow25 = [1]
pow26 = [1]
for i in range(1, n+1):
    factorial.append(factorial[-1] * i % mod)
    inverse.append(pow(factorial[-1], mod - 2, mod))
    pow25.append((pow25[-1]*25)%mod)
    pow26.append((pow26[-1]*26)%mod)

def comb(n, r, mod):
    if n < r or r < 0: return 0
    elif r == 0: return 1
    return factorial[n] * inverse[r] * inverse[n - r] % mod

n = len(s)
length = k + n
ans = 0
for i in range(n, length+1):
    temp = 1
    temp *= comb(i-1, n-1, mod)
    temp %= mod
    temp *= pow25[i-n]
    temp %= mod
    temp *= pow26[length-i]
    temp %= mod
    ans += temp
    ans %= mod
print(ans)