import sys

if sys.platform in ['ios','win32','darwin']:
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

N = int(input())
for h in range(1, 3501):
	for n in range(1, 3501):
		if 4*h*n-n*N-h*N != 0 and (h*n*N)%(4*h*n-n*N-h*N)==0 and (4*h*n-n*N-h*N)>0:
			w = int((h*n*N)//(4*h*n-n*N-h*N))
			print(h, n, w)
			sys.exit()