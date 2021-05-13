import sys
for n in sys.stdin:
	u=map(int,n.split())
	b=u[0]*u[1]
	while u[1]!=0:u=[u[1],u[0]%u[1]]
	print "%d %d"%(u[0],b/u[0])