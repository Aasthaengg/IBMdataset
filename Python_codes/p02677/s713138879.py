# :colon
import math
A,B,H,M = map(int,input().split())

def get_theta(h,m):
		cand = abs(m*6 - (h*30 + m*0.5))
		theta = math.radians([cand, 360 - cand][cand > 180])
		return theta

def cos_thm(a,b,theta):
		c_squared = (a**2) + (b**2) - (2*a*b*math.cos(theta))
		return math.sqrt(c_squared)

theta = get_theta(H,M)
if theta == 0:
		ans = abs(A-B)
elif theta == 180:
		ans = A+B
else:
		ans = cos_thm(A,B,theta)

print(ans)