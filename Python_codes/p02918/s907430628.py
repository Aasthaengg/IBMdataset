#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 14, 2020 13:00:21 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N, K = list(map(int, input().split()))
  A = input()[:-1]

  origin = 0
  for i in range(N-1):
    if A[i] == A[i+1]:
      origin += 1

  if A[0] == 'L':
    target = 'R'
  else:
    target = 'L'

  if A[-1] == 'L':
    A += 'R'
  else:
    A += 'L'

  lim = K
  pre = A[0]
  for i in range(1, N+1):
    # if pre == A[i]:
    #   pre = A[i]
    #   continue
    # if A[i] == target:
    #   pre = A[i]
    #   continue

    if (not(pre == A[i]) and not(A[i] == target)):
      lim -= 1
      if i == N:
        origin += 1
      else:
        origin += 2
      if lim <= 0:
        break
    pre = A[i]

  print(origin)


if(__name__ == '__main__'):
  main()
