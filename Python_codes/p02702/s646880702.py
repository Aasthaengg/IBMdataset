s = input()
mod = 2019
digit = 1
mstack = 0
l = [0]*mod
l[0] = 1
ans = 0

for i in s[::-1]:
    mstack += int(i)*digit
    mstack %= mod
    l[mstack] += 1

    digit *= 10
    digit %= mod

for i in l:
    ans += i*(i - 1)//2

print(ans)