# -*- coding: utf-8 -*-
N,A,B=map(int, raw_input().split())
if N==1:    #整数が1個のとき
    if A!=B:    #minとmaxが異なる場合はない
        print 0
    else:
        print 1
else:   #整数が2個以上のとき
    if B<A:
        print 0
    elif B==A:
        print 1  
    elif A<B:
        print A+B+B*(N-2)-(A+B+A*(N-2))+1