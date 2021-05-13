import math

def koch_curve(p1_x,p1_y,p2_x,p2_y,c):
	s_x = (p2_x + 2*p1_x) / 3
	s_y = (p2_y + 2*p1_y) / 3
	t_x = (2*p2_x + p1_x) / 3
	t_y = (2*p2_y + p1_y) / 3
	u_x = (math.cos(math.pi/3) * ( t_x - s_x ) - math.sin(math.pi/3) * ( t_y - s_y)) + s_x
	u_y = (math.sin(math.pi/3) * ( t_x - s_x ) + math.cos(math.pi/3) * ( t_y - s_y)) + s_y
	if c > 1:
		koch_curve(p1_x,p1_y,s_x,s_y,c-1)
		koch_curve(s_x,s_y,u_x,u_y,c-1)
		koch_curve(u_x,u_y,t_x,t_y,c-1)
		koch_curve(t_x,t_y,p2_x,p2_y,c-1)
	else:
		print("%.8f %.8f" % (p1_x,p1_y))
		print("%.8f %.8f" % (s_x, s_y))
		print("%.8f %.8f" % (u_x, u_y))
		print("%.8f %.8f" % (t_x, t_y))

if __name__ == '__main__':
	n = int(input())
	if n == 0:
		print("%.8f %.8f" % (0,0))
		print("%.8f %.8f" % (100,0))
	else:
		koch_curve(0,0,100,0,n)
		print("%.8f %.8f" % (100,0))
