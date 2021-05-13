m,n=[int(x) for x in input().split()]
connections=[[] for i in range(m+1)]
for i in range(n):
	a,b=[int(x) for x in input().split()]
	connections[a].append(b)
	connections[b].append(a)
for i in range(1,m+1):
	print(len(connections[i]))