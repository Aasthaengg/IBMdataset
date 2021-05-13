# coding: UTF-8
import sys
import numpy as np



n,k = map(int, input().split())
ansList = [False for _ in range(n+1)]

for _ in range(k):
	input()
	tmpList = list(map(int, input().split()))
	for person in tmpList:
		ansList[person] = True

print(ansList.count(False) - 1)