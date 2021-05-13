X=int(input())
ans=0
for i in range(X+1):
	ans+=i
	if ans>=X:
		print(i)
		break