import math
th = math.pi/3

def koch(p2, n, points):
	p1 = points[-1]
	x, y = p2[0]-p1[0], p2[1]-p1[1]
	s = [p1[0]+x/3, p1[1]+y/3]
	t = [p1[0]+x*2/3, p1[1]+y*2/3]
	s0t = [t[0]-s[0], t[1]-s[1]]
	s0u = [math.cos(th)*s0t[0] - math.sin(th)*s0t[1],
	       math.sin(th)*s0t[0] + math.cos(th)*s0t[1]]
	u = [s[0]+s0u[0], s[1]+s0u[1]]
	
	if n == 0:
		points.append(p2)
	else:
		koch(s, n-1, points)
		koch(u, n-1, points)
		koch(t, n-1, points)
		koch(p2, n-1, points)


if __name__ == '__main__':
	n = int(input())
	p1 = [0.0, 0.0]
	p2 = [100.0, 0.0]
	points = [p1]
	koch(p2, n, points)
	[print(*p) for p in points]