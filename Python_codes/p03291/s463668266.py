MOD = 10 **9 + 7
s = input()

n = len(s)
o = [1] * (n+1)
a = [0] * (n+1)
b = [0] * (n+1)
c = [0] * (n+1)

for i in range(n):
    if s[i] == '?':
        o[i+1] = o[i] * 3
        a[i+1] = a[i] * 3 + o[i]
        b[i+1] = b[i] * 3 + a[i]
        c[i+1] = c[i] * 3 + b[i]
    else:
        o[i+1] = o[i]
        a[i+1] = a[i]
        b[i+1] = b[i]
        c[i+1] = c[i]
        if s[i] == 'A':
            a[i+1] += o[i]
        if s[i] == 'B':
            b[i+1] += a[i]
        if s[i] == 'C':
            c[i+1] += b[i]
    o[i+1] = o[i+1] % MOD
    a[i+1] = a[i+1] % MOD
    b[i+1] = b[i+1] % MOD
    c[i+1] = c[i+1] % MOD
print(c[n])