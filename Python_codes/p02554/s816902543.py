mod = 1000000007

n = int(input())

a = 1
b = 1
c = 1
for i in range(n):
    a = a * 10 % mod
    b = b * 8 % mod
    c = c * 9 % mod


d = (a - 2 * c + b + mod) % mod
d = (d + mod) % mod
print(d)
