#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 13, 2020 08:25:55 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = [-1]+list(map(int, input().split()))

  D = [-1]*(N+1)
  for i in range(N, 0, -1):
    if i > int(N/2):
      D[i] = A[i]
    else:
      temp_sum = 0
      for j in range(N//i, 1, -1):
        temp_sum += D[i*j]
      D[i] = (temp_sum % 2) ^ A[i]

  print(sum(D[1:]))
  for i in range(1, N+1):
    if D[i]:
      print(i)


if(__name__ == '__main__'):
  main()
