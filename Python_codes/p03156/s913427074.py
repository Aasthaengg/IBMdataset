# coding: utf-8
#N, h, w = map(int,input().split())
N = int(input())
#s = list(map(str,input().split()))
a, b = map(int,input().split())
P = list(map(int,input().split()))
ans = 0
c1 = 0
c2 = 0
c3 = 0

for p in P:
    if p <= a:
        c1 += 1
    elif a < p <= b:
        c2 += 1
    else:
        c3 += 1
print(min(c1,c2,c3))