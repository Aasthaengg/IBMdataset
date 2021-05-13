n = int(input())
L = list(map(int, input().split()))

l = []

if n == 1:
	print(*L)
	exit()

if n%2 == 0:
	for i in range (0,n//2):
		l.append(L[n-1-2*i])
	for i in range (0,n//2):
		l.append(L[2*i])
else:
	for i in range (0,n//2+1):
		l.append(L[n-1-2*i])
	for i in range (0,n//2):
		l.append(L[2*i+1])

print(*l)