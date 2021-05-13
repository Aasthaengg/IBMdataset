D = [int(input()) for t in range(5)]
lag=[]
for i in range(5):
	lag.append(int(round(D[i]+4.1,-1))-D[i])
lag.pop(lag.index(max(lag)))
print(sum(D)+sum(lag))