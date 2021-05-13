#!/usr/bin/env python
#-*- coding:utf-8 -*-

def linearSearch(arr,key):
	arr.append(int(key))
	for idx,a in enumerate(arr):
		if a == key:
			if idx == (len(arr) - 1):
				return -1
			else :
				return 1
	
def main():
	Ns = int(raw_input())
	S  = map(int, raw_input().split())
	Nt = int(raw_input())
	T  = map(int, raw_input().split())

	sum_v = 0
	for key  in T:
		if linearSearch(S,key) > 0:
			sum_v += 1

	print sum_v

#def test():

if __name__ == '__main__':
	main()
	#test()