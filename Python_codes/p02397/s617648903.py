#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main(): 
	nums = []
	while True:
		x = input().split(" ")
		if x == ["0","0"]:
			break
		x.sort(key = int)
		nums.append(x)
	for i in nums:
			print(" ".join(i))
if __name__ == '__main__':
  main()