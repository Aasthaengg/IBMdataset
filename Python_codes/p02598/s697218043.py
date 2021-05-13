import math
N,K = map(int,input().split())
A = list(map(int,input().split()))

def cut(c):
    t = 0
    for a in A:
        if a<=c:
            continue
        t += math.ceil(a/c) - 1
    return t<=K

l=0
r=10**9
while((l+1)<r):
    c = (l+r)//2
    if cut(c):
        r = c
    else:
        l = c

print(r)