x, y = map(int, input().split())
tmp = 2*y - x
if tmp%3 != 0:
    print(0)
    exit()
up = tmp // 3
total = y - up*2 + up

n = total
k = up
mod = 10**9 + 7

#print(n)
#print(k)

if k == 0:
    print(1)
    exit()
try:
    modinv_table = [-1] * (k+1)
    modinv_table[1] = 1
    for i in range(2, k+1):
        modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod
except:
    k = total - up
    modinv_table = [-1] * (k + 1)
    modinv_table[1] = 1
    for i in range(2, k + 1):
        modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans

print(binomial_coefficients(n, k))