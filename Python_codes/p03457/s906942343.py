prev,pt = (0,0),0
b = True
def f(a,b): return abs(b[0]- a[0]) + abs(b[1] - a[1])
for _ in range(int(raw_input())):
	t,x,y  = map(int, raw_input().split())
	if (t - pt) < f((x,y), prev) :
		b = False
		break 

	if ((t - pt) - f((x,y), prev)) % 2:
		b = False
		break
	prev,pt = (x,y),t

print 'Yes' if b else 'No'