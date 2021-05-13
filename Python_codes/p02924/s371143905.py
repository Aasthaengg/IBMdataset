#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 14, 2020 11:34:55 by Nobody
# $Author$
# $Date$
# $URL$
__giturl__ = "$URL$"


from sys import stdin
input = stdin.readline


def main():
  N = int(input())

  print((N-1)*N//2)


if(__name__ == '__main__'):
  main()
