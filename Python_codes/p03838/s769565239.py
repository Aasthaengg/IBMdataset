import sys
input = sys.stdin.readline

# A - Simple Calculator
x, y = map(int, input().split())

if x < y:
	if x >= 0:
		print(y - x)
	elif x <= 0 and y > 0:
		if abs(x) > y:
			print(abs(x) - y + 1)
		else:	
			count = y - abs(x) + 1
		
			if count > 0:
				print(min(count, abs(x) + y))
			else:
				print(abs(x) + y)
	else:
		print(abs(x) - abs(y))
else:
	if y > 0:
		print(x- y + 2)
	elif y == 0:
		print(x + 1)
	elif x >= 0 and x >= abs(y):
		print(x - abs(y) + 1)
	elif x >= 0 and x < abs(y):
		print(abs(y) - x + 1)
	else:
		print(abs(y) - abs(x) + 2)