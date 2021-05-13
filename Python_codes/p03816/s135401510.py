import sys
from collections import Counter

if sys.platform in ['ios','win32','darwin']:
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

N = INT()
A = MAP()

C = Counter(A).most_common()
# print(C)

double = 0
for c in C:
	num, cnt = c
	# print(cnt)
	if cnt % 2 == 0:
		double += 1

if double % 2:
	print(len(C)-1)
else:
	print(len(C))