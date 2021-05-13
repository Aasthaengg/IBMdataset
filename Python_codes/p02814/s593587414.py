k, x = map(int, input().split())
l = list(map(int, input().split()))
hl = [i // 2 for i in l]
from fractions import gcd
from functools import reduce
def lcm(a, b):
    return a * b // gcd(a, b)
def lcm_list(l):
    return reduce(lcm, l, 1)
a = lcm_list(hl)
i = hl[0]
cnt = 0
while i % 2 == 0:
    cnt += 1
    i //= 2
flag = True
for i in hl:
    if i % (2 ** cnt) == 0 and i % (2 ** (cnt + 1)) != 0:
        continue
    else:
        flag = False
        break
if flag:
    print((x - a) // (a * 2) + 1)
else:
    print(0)
