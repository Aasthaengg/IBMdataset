N,M,X=map(int,input().split())
count=0
for i in range (N+1):
	for j in range(M+1):
		if i==0:
			count=N*j
			if count==X:
				print("Yes")
				exit()
		else:
			count=(N*j-(i*j)+M*i-(i*j))
			if count==X:
				print("Yes")
				exit()
print("No")