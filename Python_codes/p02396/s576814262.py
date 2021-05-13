#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main(): 
	nums = []
	while True:
		x = int(input())
		if x == 0:
			break
		nums.append(x)
	for i in range(len(nums)):
		print("Case %d: %d" % (i + 1, nums[i]))
	
if __name__ == '__main__':
  main()