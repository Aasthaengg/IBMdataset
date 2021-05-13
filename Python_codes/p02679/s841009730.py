import sys
input = sys.stdin.readline
mod = 10**9 + 7
n = int(input())
ab = [[int(x) for x in input().split()] for _ in range(n)]
from collections import defaultdict, Counter
import math

double_zero_cnt = 0 # [0, 0]の個数
a_b = [] # a/bを、約分した形で保持(a/gcd(a, b), b/gcd(a, b), 符号)
for a, b in ab:
    if a == 0 and b == 0: 
        double_zero_cnt += 1
        continue
    g = math.gcd(a, b)
    a //= g
    b //= g
    sign = 1 if a*b > 0 else -1 if a*b < 0 else 0
    a_b.append((abs(a), abs(b), sign))

c = Counter(a_b) # ベクトルごとにグループ分け
key_list = list(c.keys())

d = defaultdict(list) # [a, b] あるngなペアのそれぞれの要素の個数
for key in key_list:
    a, b, sign = key
    if d[(b, a, -sign)]: # ダブルカウントしないように
        continue 
    if c[(b, a, -sign)] != 0:
        d[(a, b, sign)] = [c[(a, b, sign)], c[(b, a, -sign)]]

ans = 1 # 積算の単位元
used_cnt = double_zero_cnt # 組めないものがあるイワシの個数(計算で使用したらカウント)
for key in d.keys():
    if d[key] == []: # 前のループで調べると[]が生まれてしまう
        continue
    x, y = d[key]
    used_cnt += (x + y)
    mul = (pow(2, x, mod) + pow(2, y, mod) - 1) % mod # このグループからは、片方ずつからしか出せない。何も選ばないがダブルカウントになる。
    ans *= mul
    ans %= mod

ans *= pow(2, n - (used_cnt), mod) # まだ使われていないイワシは好きな組み合わせ可能
ans += double_zero_cnt # 両方0のものは1つにつき自分のみの1通り
ans -= 1 # 0匹は選べない
ans %= mod
print(ans)
