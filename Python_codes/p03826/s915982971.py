# -*- coding: utf-8 -*-

#----------
A,B,C,D = list(map(int, input().rstrip().split()))
#----------
area1 = A*B
area2 = C*D

print( max(area1,area2) )
