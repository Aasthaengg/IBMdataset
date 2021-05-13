# 解説AC
# (a,b)をベクトルと考え、内積0→直行するものをとってくる。
# 全ての候補をa>0(or a=0)となるように考えて記録する。
# 第一象限に有るものを候補に考えて、それの対として第四象限にあるものを取ってくる。
# (a,b) s個、(b,-a)t個のとき、少なくとも1つ選ぶもの同士を掛け算して全体から余事象をとる
# 　2^(s+t)-(2^s-1)*(2^t-1)
# 全部選ばないやつは最後に1引いて調整
# zero,zeroのものはそれ自体の集合から1つ選ぶしかないのでzerocnt個足す

from math import gcd
from collections import defaultdict
import sys

input = sys.stdin.buffer.readline

mod = 10 ** 9 + 7
n = int(input())
cnt = 0
cnt += n
cnt10 = 0
cnt01 = 0
zerocnt = 0
kumi = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        zerocnt += 1
        continue
    elif b == 0:
        cnt10 += 1
        continue
    elif a == 0:
        cnt01 += 1
        continue
    g = gcd(a, b)
    a //= g
    b //= g
    if a < 0:
        a *= -1
        b *= -1
    kumi[(a, b)] += 1
    kumi[(b, -a)] += 0
ans = 1
cnt -= zerocnt
ans *= pow(2, cnt10 + cnt01, mod) - (pow(2, cnt10, mod) - 1) * (pow(2, cnt01, mod) - 1)
ans %= mod
cnt -= cnt10 + cnt01
for a, b in kumi.keys():
    if b <= 0:
        continue
    s = kumi[(a, b)]
    t = kumi[(b, -a)]
    ans *= pow(2, (s + t), mod) - (pow(2, s, mod) - 1) * (pow(2, t, mod) - 1)
    ans %= mod
    cnt -= s + t
if cnt > 0:
    ans *= pow(2, cnt, mod)
    ans %= mod
print((ans - 1 + zerocnt) % mod)
