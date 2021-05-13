# -*- coding: utf-8 -*-
A,B = [int(i) for i in input().split()]

if A+B >= A-B and A+B >= A*B:
    print(A+B)
elif A-B >= A+B and A-B >= A*B:
    print(A-B)
elif A*B >= A+B and A*B >= A-B:
    print(A*B)
