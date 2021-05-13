# coding: utf-8
n, m = map(int,input().split())
r = float('inf')
l = 0
L = []
for i in range(m):
    l_, r_ = map(int,input().split())
    L.append([l_,r_])
    l = max(l_, l)
    r = min(r_, r)
ans = 0
print(max(0, r-l+1))