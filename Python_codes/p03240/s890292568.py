import collections
n = int(raw_input())
pts = [map(int , raw_input().split()) for _ in range(n)]

def f(pts):
	for cx,cy in [(ii,jj) for ii in range(100+1) for jj in range(100+1)]:	
		H = min([abs(cx - x) + abs(cy - y) for x,y,h in pts if h == 0] or [+float('inf')])
		
		cc = collections.Counter()
		for x,y,h in pts:
			q = abs(cx - x) + abs(cy - y)
			if h > 0:
				Y = h + q
				if 1<=Y <= H:
					cc[Y]+=1
				else:
					cc[-1] += 1
		if len(cc) == 1:
			for k in cc:
				if 1<=k <= H:
					return k,cx,cy

h,x,y = f(pts)

print x,y,h