N,A,B = map(int,input().split());
lst = list(map(int,input().split()))

cost = 0
for i in range (1,N):
	if (lst[i]-lst[i-1])*A < B:
		cost+=((lst[i]-lst[i-1])*A)

	else:
		cost+=B 

print(cost)