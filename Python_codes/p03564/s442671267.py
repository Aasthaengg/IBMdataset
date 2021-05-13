n = int(input())
k = int(input())
x = 1
i = 0
while i < n:
	i += 1
	x = min(2*x, k+x)
print (x)