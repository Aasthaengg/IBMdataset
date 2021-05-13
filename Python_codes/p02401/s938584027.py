# coding: utf-8
# Your code here!
# ITP1_4_C


while(True):
    x,k,y=input().split()
    x=int(x)
    y=int(y)
    if k=='?':
        break
    else:
        if k=='+':
            print(x+y)
        elif k=='-':
            print(x-y)
        elif k=='*':
            print(x*y)
        elif k=='/':
            print(int(x/y))
