s = list(map(int, list(input())))

mod = 2019

mods = [0 for i in range(2019)]
mods[0] += 1

num = 0

pow10mod = 1

for i in range(len(s)):
    num = (num + s[-(i+1)] * pow10mod) % mod
    mods[num] += 1
    pow10mod = pow10mod * 10 % mod

ans = 0

for i in range(2019):
    m = mods[i]
    ans += (m * (m-1) // 2)


print(int(ans))
