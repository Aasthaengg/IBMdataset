from math import *
PI = 3.1415926535898
while True:
    try:
    	k = raw_input()
    	if len(k) > 0:
	    	a, b, x, y = map(float, k.strip().split(' '))
	    	print pow((a-x)*(a-x)+(b-y)*(b-y), 0.5)
    except EOFError:
        break