#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	a, b = [int(i) for i in input().split(" ")]
	print("%d %d %f" % (a // b, a % b, a / b))
if __name__ == '__main__':
  main()