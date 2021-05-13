# -*- coding: utf-8 -*-
h,w = list(map(int,input().split()))
d = [list(map(int,input().split())) for i in range(h)]

ret=[]
ra = ret.append
for hi in range(h):
    for wi in range(w):
        if d[hi][wi]%2==1:
            if wi!=w-1:
                d[hi][wi]-=1
                d[hi][wi+1]+=1
                ra([hi,wi,hi,wi+1])
            else:
                if hi!=h-1:
                    d[hi][wi]-=1
                    d[hi+1][wi]+=1
                    ra([hi,wi,hi+1,wi])
                else:
                    pass

print(len(ret))
for i in ret:
    i = list(map(lambda x:x+1,i))
    print(" ".join(list(map(str,i))))