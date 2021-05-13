#A
S = input()

print("ABC" if S == 'ARC' else 'ARC')

##D
#N,K = map(int,input().split())
#A = list(map(int,input().split()))

#list = []
#list.append(1)
#last = 0
#for n in range(N):
#	inp = A[list[-1] - 1]
#	if inp in list:
#		last = inp
#		break
#	else:
#		list.append(inp)

#head = list.index(last)

#remain = (K - head) % (len(list) - head)

#print(list[head + remain])


##C
#N,M,X = map(int,input().split())
#C = []
#A = []

#for c in range(N):
#	p = list(map(int,input().split()))
#	C.append(p[0])
#	A.append(p[1:])

#minCost = sum(C)
#result = -1

#for i in range(2 ** N):
#	rikai = [0] * M
#	cost = 0
#	for n in range(N):
#		if i >> n & 1 == 0:
#			continue
#		cost+=C[n]		
#		for m in range(M):
#				rikai[m]+=A[n][m]
	
				
#	ok = True
#	if all(x >= X for x in rikai):
#		if result == -1:
#			result = cost
#		else:
#			result = min(result,cost)


#print(result)
