mod = 10 ** 9 + 7
sl = list(input())

a = 0
ab = 0
abc = 0
p = 1
for s in sl:
    if s == "A":
        a += p
        a %= mod
    elif s == "B":
        ab += a
        ab %= mod
    elif s == "C":
        abc += ab
        abc %= mod
    elif s == "?":
        abc = 3*abc + ab
        abc %= mod
        ab = 3*ab + a
        ab %= mod
        a = 3*a + p
        a %= mod
        p *= 3
        p %= mod
print(abc)

