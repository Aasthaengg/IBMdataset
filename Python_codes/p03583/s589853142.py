# coding: utf-8
import math
n=int(input())
flg=False
for i in range(1, 3501):
    for j in range(1, 3501):
        a=i
        b=j
        if 4*a*b-n*(a+b)!=0:
            c=n*a*b/(4*a*b-n*(a+b))
            if c==int(c) and c>0:
                c=int(c)
                flg=True
                break
    if flg:
        break
print(a,b,c)