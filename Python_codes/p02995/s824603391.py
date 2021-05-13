#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 04:11:55 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


import math
from sys import stdin
input = stdin.readline


def main():
  A, B, C, D = list(map(int, input().split()))

  # divisible by C
  dc = B//C - (A-1)//C

  # divisible by D
  dd = B//D - (A-1)//D

  lcm = C * D // math.gcd(C, D)
  # divisible by (C and D)
  dcd = B//lcm - (A-1)//lcm

  # print(f'B-A+1: {B-A+1}')
  # print(f'dc   : {dc}')
  # print(f'dd   : {dd}')
  # print(f'lcm  : {lcm}')
  # print(f'dcd  : {dcd}')
  print((B-A+1) - dc - dd + dcd)


if(__name__ == '__main__'):
  main()
