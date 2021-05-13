import sys

s = input().split(' ')
x, y = int(s[0]), int(s[1])

if (x > 8 or y > 8):
	print (":(")
else:
	print ("Yay!")