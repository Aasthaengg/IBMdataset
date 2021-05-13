# -*- coding: utf-8 -*-

A,B,C = [int(i) for i in input().rstrip().split()]


print( "Yes" if (A+B) >= C else "No" )