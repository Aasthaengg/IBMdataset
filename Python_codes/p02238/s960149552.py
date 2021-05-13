import sys

#sys.setrecursionlimit(100000)
u=[]
k=[]
v=[]

time = 0

n=int(sys.stdin.readline().strip())
yattayatu=[False for i in range(n)]

s=[0 for i in range(n)]
f=[0 for i in range(n)]

for i in range(n):
	inp = sys.stdin.readline().strip().split(" ")
	inp = list(map(lambda x: int(x), inp))
	u.append(inp[0])
	k.append(inp[1])
	v.append(inp[2:])


def func(nodeid):
	global time
	if(yattayatu[nodeid-1]==True):
		return
	yattayatu[nodeid-1]=True
	time += 1
	s[nodeid-1] = time
	for i in range(k[nodeid-1]):
		func(v[nodeid-1][i])
	time +=1
	f[nodeid-1]=time
	return

for i in range(n):
	func(i+1)

for i in range(n):
	print(str(i+1)+" "+str(s[i])+" "+str(f[i]))