#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 12, 2020 07:40:30 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  D = [int(input()) for _ in range(N)]

  print(len(set(D)))


if(__name__ == '__main__'):
  main()
