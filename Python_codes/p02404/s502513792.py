#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	boxes = []
	while True:
		h, w = [int(i) for i in input().split(" ")]
		if h == 0 and w == 0:
			break
		boxes.append([h, w])
	for i in boxes:
		print("#"* i[1])
		for j in range(i[0] - 2):
			print("#"+ "." * (i[1] - 2) + "#")
		print("#"* i[1])
		print()
	return
if __name__ == '__main__':
  main()