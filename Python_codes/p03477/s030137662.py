# -*- coding: utf-8 -*-

A,B,C,D = [int(i) for i in input().rstrip().split()]

L=A+B
R=C+D

print( "Left" if L>R else "Balanced" if L==R else "Right" )