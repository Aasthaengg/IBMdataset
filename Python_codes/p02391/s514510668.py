#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	nums = input().split(" ")
	a , b= int(nums[0]),int(nums[1])
	if a < b:
		return "a < b"
	elif a == b:
		return "a == b"
	else:
		return "a > b"
if __name__ == '__main__':
  print(main())