#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	num = int(input())
	for i in range(num):
		tri = [int(x) for x in input().split(" ")]
		tri.sort()
		if tri[2] ** 2 == tri[0] ** 2 + tri[1] ** 2:
			print("YES")
		else:
			print("NO")
			
if __name__ == '__main__':
  main()