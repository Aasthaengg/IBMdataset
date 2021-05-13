#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	input()
	nums = [int(i) for i in input().split(" ")]
	print("%d %d %d" % (min(nums),max(nums),sum(nums)))
if __name__ == '__main__':
  main()