n,a,b=map(int,input().split())

if n == 1:
	if a != b:
		print(0)
		exit()
	else:
		print(1)
		exit()

print(max(0, b*(n-1)+a-a*(n-1)-b+1))