A,B,K=map(int,input().split(' '))
l=[A,B]
for i in range(K):
	p=l[i%2]
	l[i%2] = (p-(p%2))/2
	l[(i+1)%2] += (p-(p%2))/2
print(' '.join([str(int(x)) for x in l]))