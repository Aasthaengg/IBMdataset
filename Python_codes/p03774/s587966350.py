def readInts():
	return list(map(int, input().split()))

n,m = readInts()
ab = [readInts() for i in range(n)]
cd = [readInts() for i in range(m)]

for i in ab:
	ansv = float("inf")
	ansi = -1
	for j in range(len(cd)):
		if abs(i[0]-cd[j][0])+abs(i[1]-cd[j][1])<ansv:
			ansv = abs(i[0]-cd[j][0])+abs(i[1]-cd[j][1])
			ansi = j+1
	print(ansi)