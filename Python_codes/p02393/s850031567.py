#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	nums = input().split(" ") 
	nums.sort()
	return " ".join(nums)
	
if __name__ == '__main__':
  print(main())