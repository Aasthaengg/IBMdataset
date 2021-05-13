n,q = map(int,raw_input().split(" "))
task = [raw_input().split(" ") for i in range(n)]
c= 0
while task:
	name,time = task.pop(0)
	e = int(time) - q
	if e > 0:
		c+= q
		task.append([name,e])
	else:
		c+= int(time)
		print name+" "+str(c)