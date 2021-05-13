# -*- coding: utf-8 -*-

a,b = [int(i) for i in input().rstrip().split()]


print( (a-1)+1 if b>=a else (a-1) )