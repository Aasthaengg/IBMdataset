#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	res = []
	while True:		
		try:
			res.append(int(eval(input())))
		except:
			[print(i) for i in res]
			return
if __name__ == '__main__':
  main()