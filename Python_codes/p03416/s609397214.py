x,y=map(int, input().split())
cnt=0
for i in range(9):
	for j in range(10):
		for k in range(10):
			a=10001*(i+1)+100*k+1010*j
			if y>=a>=x:
				cnt+=1
print(cnt)