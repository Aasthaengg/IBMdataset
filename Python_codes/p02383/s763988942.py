

u,s,e,w,n,b = map(int,input().split())
roll = input()
for i in roll:
	if i == "E":
		tmp = e
		e = u
		u = w
		w = b
		b = tmp
	elif i == "S":
		tmp = s
		s = u
		u = n
		n = b
		b = tmp
	elif i == "W":
		tmp = w
		w = u
		u = e
		e = b
		b = tmp
	elif i == "N":
		tmp = n
		n = u
		u = s
		s = b
		b = tmp

print(u)