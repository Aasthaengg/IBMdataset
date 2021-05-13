from math import gcd
from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7

N = int(input())
pp = defaultdict(int)
pn = defaultdict(int)
p_zero = 0
zero_p = 0
zero = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a == b == 0:
        zero += 1
    elif a == 0:
        zero_p += 1
    elif b == 0:
        p_zero += 1
    elif a * b > 0:
        g = gcd(a, b)
        a = abs(a) // g
        b = abs(b) // g
        pp[(a, b)] += 1
    else:
        g = gcd(a, b)
        a = abs(a) // g
        b = abs(b) // g
        pn[(a, b)] += 1

checked = defaultdict(bool)
ans = 1

#(a,b), (c,d)
for (x, y), v in pp.items():
    checked[(x, y)] = True
    R = 0
    R += pow(2, v, mod) - 1
    R += pow(2, pn[(y, x)], mod) - 1
    R += 1
    ans = ans * R % mod

for (x, y), v in pn.items():
    if checked[(y, x)]:
        continue
    R = pow(2, v, mod)
    ans = ans * R % mod

#(0, x), (y, 0)
R = pow(2, zero_p, mod) - 1
R += pow(2, p_zero, mod) - 1
R += 1
ans = ans * R % mod

# (0,0)
ans = (ans + zero) % mod

# 空はダメ
ans = (ans - 1 + mod) % mod

print(ans)