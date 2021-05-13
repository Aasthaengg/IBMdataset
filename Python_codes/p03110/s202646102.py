import itertools
import math
import fractions
import functools

n = int(input())
dic = {"JPY":0, "BTC":0}
for i in range(n):
    l = list(input().split())
    if l[1] == 'JPY':
        dic["JPY"] += float(l[0])
    if l[1] == 'BTC':
        dic["BTC"] += float(l[0])

print(dic["JPY"] + 380000*dic["BTC"])