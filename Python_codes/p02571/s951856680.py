from sys import stdin

input = stdin.readline

s = input().strip()
t = input().strip()

ns = len(s)
nt = len(t)

def cnt(a,b):
    return sum(1 for aa,bb in zip(a,b) if aa != bb)

res = nt
for i in range(ns - nt + 1):
    res = min(res,cnt(s[i:i+nt],t))

print(res)