import math
N,A,B = map(int,input().split())
h = list(int(input())for i in range(N))

def func(l,r):
    if l == r:
        return l
    c = (l+r)//2
    hoge = 0
    for i in h:
        hoge += max(math.ceil((i-(B*c))/(A-B)),0)
    if hoge > c:
        return func(c+1,r)
    elif hoge < c:
        return func(l,c)
    else:
        return c

print(func(0,10**9+7))