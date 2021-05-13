MOD = 10**9+7
d = dict()
s = int(input())
d[0], d[1], d[2], d[3], d[4], d[5] = 1, 0, 0, 1, 1, 1
def mod(x):
    return (x%MOD + MOD)%MOD

def add(a, b):
    return mod(mod(a) + mod(b))

def ans(n):
    if n in d:
        return d[n]
    else:
        total = 0
        for i in range(3, n+1):
            if n-i>=0:
                # print(i, n-i)
                total = add(total, ans(n-i))
                # print(total)
        d[n] = total
        return d[n]

print(ans(s))


