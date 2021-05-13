# -*- coding: utf-8 -*-

## Library

from fractions import gcd
import math
from math import ceil,floor
import collections

## input

# n=int(input())
# A,B,C,D=map(int, input().split())
# string = input()
# list = list(map(int, input().split()))

A,B=map(int, input().split())

## Logic

if (A*B)%2 == 0:
    print("Even")
else:
    print("Odd")

## output

