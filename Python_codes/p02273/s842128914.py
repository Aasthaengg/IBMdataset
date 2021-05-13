import math
n = int(raw_input())

p1_x = float(0)
p1_y = float(0)
p2_x = float(100)
p2_y = float(0)

def KC(i, n, x1, y1, x2, y2):
	v = [0]*5
	w = [0]*5
	if i < n:
		v[0] = x1
		w[0] = y1
		v[1] = (2*x1+x2)/3.0
		w[1] = (2*y1+y2)/3.0
		v[2] = (x1+2*x2)/3.0
		w[2] = (y1+2*y2)/3.0
		v[3] = (v[2] - v[1])*math.cos(math.pi/3) - (w[2] - w[1])*math.sin(math.pi/3) + v[1]
		w[3] = (w[2] - w[1])*math.cos(math.pi/3) + (v[2] - v[1])*math.sin(math.pi/3) + w[1]
		v[4] = x2
		w[4] = y2
		KC(i+1, n, v[0], w[0], v[1], w[1])
		print v[1], w[1]
		KC(i+1, n, v[1], w[1], v[3], w[3])
		print v[3], w[3]
		KC(i+1, n, v[3], w[3], v[2], w[2])
		print v[2], w[2]
		KC(i+1, n, v[2], w[2], v[4], w[4])

print p1_x, p1_y
KC(0, n, p1_x, p1_y, p2_x, p2_y)
print p2_x, p2_y