#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 13:52:40 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  sum_ = 0
  for i in range(N):
    temp_sum = min(A[i]+A[i+1], B[i])
    sum_ += temp_sum
    A[i+1] -= (temp_sum - min(A[i], B[i]))

  print(sum_)


if(__name__ == '__main__'):
  main()
