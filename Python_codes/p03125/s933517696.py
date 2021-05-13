# -*- coding: utf-8 -*-

A,B = [int(i) for i in input().rstrip().split()]

print( (A+B) if B%A == 0 else (B-A) )
