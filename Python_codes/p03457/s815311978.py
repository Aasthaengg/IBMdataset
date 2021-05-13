n = int(input())
t = 0
x = 0
y = 0
for _ in range(n):
	nt, nx, ny = map(int,input().split())
	sa = nt-t
	t = nt
	kyori = abs(nx-x) + abs(ny-y)
	x = nx
	y = ny
	if kyori > sa or (sa-kyori) % 2 == 1:
		print("No")
		exit()
print("Yes")