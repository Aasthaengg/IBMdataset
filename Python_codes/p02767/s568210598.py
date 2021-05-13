N=int(input())
X=list(map(int, input().split()))
ans=[0]*100

for i in range(100):
	P=i+1
	a=0
	for x in X:
		a+=(x-P)**2
	ans[i]=a

print(min(ans))