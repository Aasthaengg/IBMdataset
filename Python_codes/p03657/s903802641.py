# -*- coding: utf-8 -*-

a, b = map(int, input().split())

isPossible = False

if a%3 == 0:
    isPossible = True
if b%3 == 0:
    isPossible = True
if (a+b)%3 == 0:
    isPossible = True

if isPossible:
    print("Possible")
else:
    print("Impossible")