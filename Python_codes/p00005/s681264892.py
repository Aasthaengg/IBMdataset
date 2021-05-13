import math
import sys

while True:
	try:
		a,b = map(int, input().split())
		p = a
		q = b
		while True:
			r = p%q
			if r == 0:
				x = q
				break
			else:
				p = q
				q = r
		i = 1
		while True:
			if a*i%b == 0:
				y = a*i
				break
			else:
				i = i+1
		print(x,y)
	except EOFError:
		break