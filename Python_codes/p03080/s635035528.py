# B - Red or Blue
import sys
input = sys.stdin.readline
n = int(input())
huts = input()
r = 0
b = 0
for i in range(n):
	if huts[i] == "R":
		r += 1
	else:
		b += 1
if r > b:
	print("Yes")
else:
	print("No")