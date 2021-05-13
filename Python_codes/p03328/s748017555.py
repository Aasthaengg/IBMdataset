# -*- coding: utf-8 -*-

a,b = list(map(int, input().rstrip().split()))
#-----

n = b-a-1
x1 = n*(n+1)/2 - a
#x2 = (n+1)*(n+2)/2 - b

print( int(x1) )
