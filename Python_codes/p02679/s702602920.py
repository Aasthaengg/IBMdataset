import sys
import math
from collections import defaultdict

input = sys.stdin.buffer.readline
MOD = 1000000007
N = int(input())
dd = defaultdict(int)
count = 1
iwashi = [list(map(int, input().split())) for _ in range(N)]


checked = defaultdict(bool)
zeros = 0

for i in range(N):
    if iwashi[i][0] == iwashi[i][1] == 0:
        zeros += 1
        continue
    iw = iwashi[i]
    gcd_iw = math.gcd(iw[0], iw[1])
    if gcd_iw != 0:
        iw = list(map(lambda x: x // gcd_iw, iw))
    if iw[0] < 0:
        iw = list(map(lambda x: -x, iw))
    if iw[0] == 0 and iw[1] < 0:
        iw = list(map(lambda x: -x, iw))
    dd[tuple(iw)] += 1

for key, val in dd.items():
    if checked[key]:
        continue
    vert_key = (key[1], -key[0]) if key[1] > 0 else (-key[1], key[0])
    vert_val = dd[vert_key] if vert_key in dd else 0
    count *= (pow(2, val, MOD) - 1) + (pow(2, vert_val, MOD) - 1) + 1
    count %= MOD
    checked[vert_key] = True

# 0匹入れる場合を除外
count -= 1

count += zeros
print(count % MOD)
