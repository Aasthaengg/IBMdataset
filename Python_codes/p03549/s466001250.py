from math import ceil
n, m = map(int, input().split())

base = (n-m)*100+1900*m
allok = pow(2,m)

"""
1回目はbase秒かかる
2回目の期待値は、1回目の時点から考えるとbase + (allok-1)*y
"""

print(base*allok)

