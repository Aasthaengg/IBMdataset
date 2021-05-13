#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 14, 2020 12:42:18 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  B = list(map(int, input().split()))

  A = [0]*(N)
  A[0] = B[0]
  A[1] = B[0]
  for i in range(1, N-1):
    if A[i] > B[i]:
      A[i] = B[i]
    A[i+1] = B[i]

  # print(A)
  print(sum(A))


if(__name__ == '__main__'):
  main()
