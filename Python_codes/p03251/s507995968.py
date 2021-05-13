n,m,x,y=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))

xl=max(X)
ys=min(Y)

for z in range(x+1,y+1):
	if xl<z<=ys:
		print("No War")
		break
else:
	print("War")