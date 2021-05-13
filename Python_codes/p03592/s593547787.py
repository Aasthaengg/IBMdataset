import sys

n,m,k = map(int, input().split())

for a in range(n):
	if n-2*a == 0:
		continue
	b = ((k-a*m))/(n-2*a)
	if (b >= 0) and (b <= m) and (b%1 == 0):
		print("Yes")
		sys.exit()

print("No")