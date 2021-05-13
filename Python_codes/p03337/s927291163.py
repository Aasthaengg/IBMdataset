# -*- coding: utf-8 -*-

A,B = list(map(int, input().rstrip().split()))
#-----

print( max(A+B,A-B,A*B) )
