import sys
from bisect import bisect_left as bl
from collections import defaultdict as dd
input = sys.stdin.readline
S = list(input())[: -1]
d = dd(list)
mod = 10 ** 9 + 7
res = 0
for i in range(len(S)):
  d[S[i]].append(i)
for i in range(len(S)):
  if S[i] == "B":
    l = bl(d["A"], i)
    m = bl(d["?"], i)
    r = bl(d["C"], i)
    res += l * (len(d["C"]) - r) * pow(3, len(d["?"]), mod)
    res %= mod
    res += m * (len(d["C"]) - r) * pow(3, max(len(d["?"]) - 1, 0), mod) * (len(d["?"]) > 0)
    res %= mod
    res += l * (len(d["?"]) - m) * pow(3, max(len(d["?"]) - 1, 0), mod) * (len(d["?"]) > 0)
    res %= mod
    res += m * (len(d["?"]) - m) * pow(3, max(len(d["?"]) - 2, 0), mod) * (len(d["?"]) > 1)
    res %= mod
  elif S[i] == "?":
    l = bl(d["A"], i)
    m = bl(d["?"], i)
    r = bl(d["C"], i)
    res += l * (len(d["C"]) - r) * pow(3, len(d["?"]) - 1, mod)
    res %= mod
    res += m * (len(d["C"]) - r) * pow(3, max(len(d["?"]) - 2, 0), mod) * (len(d["?"]) > 1)
    res %= mod
    res += l * (len(d["?"]) - m - 1) * pow(3, max(len(d["?"]) - 2, 0), mod) * (len(d["?"]) > 1)
    res %= mod
    res += m * (len(d["?"]) - m - 1) * pow(3, max(len(d["?"]) - 3, 0), mod) * (len(d["?"]) > 2)
    res %= mod
  #print(res, i)
print(res)