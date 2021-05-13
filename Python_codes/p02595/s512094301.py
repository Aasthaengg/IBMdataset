N,D=(int(x) for x in input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]


count=0
for i in range(N) :
 	z=x[i]**2+y[i]**2
 	if z<=D**2 :
		 count+=1
print(count)