import sys
input = sys.stdin.readline

# A - Colorful Slimes 2
N = int(input())
a = list(input().split())
prev = a[0]

for i in range(1, N):
	if a[i] == prev:
		a[i] = 'changed'
	
	prev = a[i]

print(a.count('changed'))