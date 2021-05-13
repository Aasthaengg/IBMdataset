import sys

N,A,B=(int(x) for x in input().split())

x=[int(t.strip()) for t in input().split()]

gap=[]
for i in range(N-1):
	gap.append(x[i+1]-x[i])

total=0
for i in range(N-1):
	if gap[i]*A < B :
		total += gap[i]*A
	else:
		total += B
		
print(total)