#import numpy

N = int(input())

C = [int(i) for i in input().split()] 
V = [int(i) for i in input().split()]

ans = []
for i in range(N):
	if(C[i]-V[i]>0):
		ans.append(C[i]-V[i])
		ans.sort(reverse=True)

#x = numpy.prod(ans)
print(sum(ans))