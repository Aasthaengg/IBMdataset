x=[]
for i in range(3):
	x.append(list(map(int, input().split())))

N=int(input())

b = []
for i in range(N):
	b.append(int(input()))

for i in range(3):
	for j in range(3):
		if x[i][j] in b:
			x[i][j]=0

import numpy as np

if min(np.sum(x, axis=0))==0:
	kotae='Yes'
elif min(np.sum(x, axis=1))==0:
	kotae='Yes'
elif x[0][0]==0 and x[1][1]==0 and x[2][2]==0:
	kotae='Yes'
elif x[2][0]==0 and x[1][1]==0 and x[0][2]==0:
	kotae='Yes'
else:
	kotae='No'

print(kotae)