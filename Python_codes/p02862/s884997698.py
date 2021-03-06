x, y = map(int,input().split())
p = 10 ** 9 + 7
if (x + y) % 3 != 0 or 2*x < y or 2*y < x:
    print(0)
    exit()
a = (2 * y -x) // 3
b = (2 * x -y) // 3

n = a + b
fac = [0] * (n + 1)
fac[0] = 1
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % p
def mcomb(n,k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k],p - 2, p) * pow(fac[k], p - 2, p) % p

print(mcomb(n,a))