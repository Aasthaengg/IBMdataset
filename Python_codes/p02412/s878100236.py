n = 1
x = 1
while n!=0 or x!=0:
	n,x = [int(i) for i in input().split()]
	if n!=0 or x!=0:
		list = [int(i) for i in range(1,n+1)]
		count = 0
		for i in range (1,n-1):
			for j in range(i+1,n):
				for k in range(j+1,n+1):
					if (i + j + k) == x:
						count += 1
		print(count)