II = lambda: int(input())
SI = lambda: input()
LI = lambda: list(map(int,input().split()))
MI = lambda: map(int,input().split())
n = II()
d = [[0,0,0] for i in range(n)]
for i in range(n):
	a,b,c = MI()
	if i == 0:
		d[0][0] = a
		d[0][1] = b
		d[0][2] = c
	else:
		d[i][0] = max(d[i-1][1],d[i-1][2])+a
		d[i][1] = max(d[i-1][0],d[i-1][2])+b
		d[i][2] = max(d[i-1][1],d[i-1][0])+c
print(max(d[-1]))