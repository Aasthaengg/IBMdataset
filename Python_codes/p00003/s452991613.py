N = int(input())
for i in range(N):
	line = input()
	l = [None]*3
	l[0] = int(line.split()[0])
	l[1] = int(line.split()[1])
	l[2] = int(line.split()[2])
	l.sort()
	if l[0]**2+l[1]**2==l[2]**2:
		print("YES")
	else:
		print("NO")