import numpy as np


N = int(input().strip())
alist = list(map(int,input().strip().split()))

alist = np.array(alist)
alistp = np.abs(alist)
maxind = np.where(alistp==alistp.max())[0][0]

if alist[maxind]>0:
	positive = True
else:
	positive = False

count = 0
process = []
for i in range(N):
	if alist[i]*alist[maxind]<0:
		alist[i] = alist[i]+alist[maxind]
		count = count+1
		process.append([maxind,i])

if positive==True:
	for i in range(N-1):
		alist[i+1] = alist[i+1]+alist[i]
		count = count+1
		process.append([i,i+1])
else:
	for i in range(N-1,0,-1):
		alist[i-1] = alist[i-1]+alist[i]
		count = count+1
		process.append([i,i-1])

print(count)
for i in range(count):
	processi = process[i]
	print(processi[0]+1,processi[1]+1)
