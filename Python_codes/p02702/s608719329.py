s = input()
modl = [0]*2019
modl[0] = 1
mstack = 0
digit = 1
ans = 0

for i in s[::-1]:
    mstack += int(i) * digit
    mstack %= 2019
    modl[mstack] += 1
    digit = digit*10%2019

for i in modl:
    ans += i*(i - 1)//2

print(ans)