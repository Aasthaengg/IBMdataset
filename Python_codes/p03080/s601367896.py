import sys
input = sys.stdin.readline

# B - Red or Blue
N = int(input())
s = input()

red = s.count('R')
blue = N -red

if red > blue:
	print('Yes')
else:
	print('No')