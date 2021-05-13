# -*- coding: utf-8 -*-

a,b,c,k=map(int,input().split())

if abs(a-b)>1000000000000000000:
    print("Unfair")
else:
    if k%2==1:
        print((b-a))
    else:
        print((a-b))
