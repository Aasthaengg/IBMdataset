import sys
input = sys.stdin.readline

# A - Beginning
N = input().split()
N.sort()

if ''.join(N) == '1479':
	print('YES')
else:
	print('NO')
