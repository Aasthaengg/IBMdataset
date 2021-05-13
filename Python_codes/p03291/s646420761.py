s = input()
MOD = 10**9+7

o = 1
a = 0
b = 0
c = 0

for i in s:
    if i == "A":
        a += o
    elif i == "B":
        b += a
    elif i == "C":
        c += b
    else:
        o, a, b, c = o*3, o+a*3, a+b*3, b+c*3

    o %= MOD
    a %= MOD
    b %= MOD
    c %= MOD

print(c)