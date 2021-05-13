n = list(map(int,input().split()))
for i in list(set(n)):
	c = n.count(i)
	if c==1:
		print(i)
		exit()
