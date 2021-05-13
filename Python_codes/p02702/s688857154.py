import sys
from collections import defaultdict as de


readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prl = lambda x: print(*x ,sep='\n')

s = ns()
digit = 1
ans = 0
num = 0
amari = de(int)
amari[0] = 1
"""
大筋のやり方は
https://drken1215.hatenablog.com/entry/2020/04/29/171300
を参照。

「この下のfor文について」
1211400を考える。
1万の桁を考えるとき
digit = 10000
digit = 1924 mod 2019
11400 = 10000 + 1400 = 1924 + 1400 = ans mod 2019
つまり、ある桁までの2019のあまりはその一つ下の桁までのあまりと
その桁の数*桁のあまりを足したもののあまりである
"""

for i in s[::-1]:
    num = num + int(i) * digit
    num %= 2019
    digit *= 10
    digit %= 2019
    amari[num] += 1

for j in amari.values():
    ans += j*(j-1)//2

print(ans)