import sys
sys.setrecursionlimit(10**7)
n = int(input())

def rec(s, mx, l):
    if l >= n:
        print("".join([chr(ord("a") + x) for x in s]))
        return
    for x in range(mx+2):
        rec(s+[x], max(mx, x), l+1)

rec([0], 0, 1)
