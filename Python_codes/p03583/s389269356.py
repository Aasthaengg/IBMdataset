# -*- coding: utf-8 -*-
N=input()

for a in range(1,3501):
    for b in range(1,3501):
        if (4*a*b-N*(b+a))!=0:   #Cの計算式の分母がゼロではない
            if (N*a*b)%(4*a*b-N*(b+a))==0: #Cの計算式
                c=(N*a*b)/(4*a*b-N*(b+a))
                if 0<c:
                    print a,b,c
                    quit()