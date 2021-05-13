
n, a, b = [ int(v) for v in input().split() ]
town_list = [ int(v) for v in input().split() ]
fatigue_list = [ 0 for i in range(n) ]

for i in range(n-1):
	d = town_list[i+1] - town_list[i]
	fatigue_list[i+1] = fatigue_list[i] + min(a*d,b)
print(fatigue_list[-1])
