import sys
import math

if sys.platform in ['ios','win32','darwin']:
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

N, A, B = MAP()
C = MAP()

ans = 0
for i in range(N-1):
	dist = C[i+1]-C[i]
	if A*dist > B:
		ans += B
	else:
		ans += A*dist

print(ans)