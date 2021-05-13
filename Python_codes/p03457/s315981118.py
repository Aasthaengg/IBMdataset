# ABC_086_C_Traveling
N = int(input())
txy = [map(int, input().split()) for _ in range(N)]
t, x, y = [list(i) for i in zip(*txy)]
t.insert(0, 0)
x.insert(0, 0)
y.insert(0, 0)
can = True
distX = [0]*(N)
distY = [0]*(N)
dist = [0]*(N)
time = [0]*(N)

# distance
for i in range(N):
	distX[i] = abs(x[i]-x[i+1])
	distY[i] = abs(y[i]-y[i+1])
	dist[i] = distX[i]+distY[i]
	time[i] = t[i+1]-t[i]
	if dist[i] > time[i]:
		can = False
		break

# parity
for i in range(N):
	if (dist[i]-time[i]) % 2 == 1:
		can = False
		break

if can == True:
	print("Yes")
else:
	print("No")
