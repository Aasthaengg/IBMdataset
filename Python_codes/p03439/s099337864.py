n=int(input())

def output(x):
	print(x,flush=True)
	nxt=input()
	if nxt=="Vacant":
		exit()
	return nxt=="Male"

Lgen=output(0)
Rgen=output(n-1)

l=0
r=n-1
while True:
	m=(l+r)//2
	gen=output(m)
	if gen==Lgen:
		if (m-l)%2:
			r=m
			Rgen=gen
		else:
			l=m
			Lgen=gen
	else:
		if (m-l)%2:
			l=m
			Lgen=gen
		else:
			r=m
			Rgen=gen