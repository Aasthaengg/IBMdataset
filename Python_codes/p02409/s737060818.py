import sys
n=int(input())
data={}
for i in range(1,5):
	for j in range(1,4):
		for k in range(1,11):
			data[(i,j,k)]=0
			

for i in range(1,n+1):
	b,r,f,v=map(int,input().split())
	data[(b,r,f)]+=v

for i in range(1,5):
	for j in range(1,4):
		for k in range(1,11):
			sys.stdout.write(' '+str(data[(i,j,k)]))
		print('')
	if i<4:
		print('#'*20)