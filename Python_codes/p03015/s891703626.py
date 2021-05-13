l = input().rstrip()
n = len(l)

mod = 10**9 + 7
c = 1
d = 0
for i in range(n):
    d *= 3
    if l[i] == '1':
        d += c
        c <<= 1
    d %= mod
    c %= mod

print((c+d)%mod)