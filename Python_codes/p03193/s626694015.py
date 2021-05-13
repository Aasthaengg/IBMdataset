i, w, h =  map(int, raw_input().split())

total = 0 

for _ in range(i):
	x,y =  map(int, raw_input().split())
	if w<=x and h<=y:
		total +=1

print total		