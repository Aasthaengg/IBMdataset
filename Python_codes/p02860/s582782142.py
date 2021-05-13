import sys
input = sys.stdin.readline

n = int(input())
s = input()[:-1]

if n & 1: print('No')
else:
	if s[:n//2] == s[n//2:]: print('Yes')
	else: print('No')