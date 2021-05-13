n=int(input())

def out(x):
	print(x,flush=True)
	nxt=input()
	if nxt=="Vacant":
		exit()
	return nxt=="Male"

Lgen=out(0)
Rgen=out(n-1)

l,r=0,n-1
while True:
	m=(l+r)//2
	gen=out(m)
	if (m-l)%2==int(gen==Lgen):
		r=m
		Rgen=gen
	else:
		l=m
		Lgen=gen