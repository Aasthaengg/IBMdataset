import math

n = int(input())
mod = 10 ** 9 + 7

ab = {}
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        pass
    elif a == 0:
        b = 1
    else:
        gcd = math.gcd(a, b)
        a //= gcd
        b //= gcd
        if a < 0:
            a, b = -a, -b
    num = (a, b)
    ab.setdefault(num, 0)
    ab[num] += 1
bin_n = [2]
for i in range(len(bin(n)) - 3):
    temp = bin_n[-1]
    temp = temp ** 2
    temp %= mod
    bin_n.append(temp)
def beki2(n):
    num = bin(n)
    temp = 1
    for i in range(len(num) - 2):
        if num[-i-1] == "1":
            temp *= bin_n[i]
            temp %= mod
    return temp

ans = 0
if (0, 0) in ab.keys():
    temp2 = ab[(0, 0)]
    ans += temp2
    n -= temp2
s = set(ab.keys())
pairs = []
for i in ab.keys():
    if i == (0, 0):
        continue
    else:
        a, b = i[0], i[1]
        if (-b, a) in s:
            pairs.append([ab[(a, b)], ab[(-b, a)]])
temp3 = 1
for i in range(len(pairs)):
    num2 = pairs[i][0]
    num3 = pairs[i][1]
    temp3 *= (beki2(num2) + beki2(num3) - 1)
    n = n- num2 - num3
    temp3 %= mod
temp3 *= beki2(n)
temp3 -= 1
temp3 %= mod
ans += temp3
ans %= mod
print(ans)