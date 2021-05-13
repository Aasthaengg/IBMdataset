l, r = list(map(int, input().split()))

MOD = 2019

a = 0

if r - l >= MOD:
    a = 0

else:
    x = l % MOD
    y = r % MOD
    if x > y:
        a = 0
    else:
        a = 2018
        for i in range(x, y):
            for j in range(i+1, y+1):
                a = min(a, i * j % MOD)

print(a)