import copy
n=int(input())
num=input().split()
numa=copy.copy(num)
numb=copy.copy(num)

#buble
for i in range(0,n):
	a=0
	for j in range(n-1,i,-1):
		if numa[j][1:]<numa[j-1][1:]:
			a=numa[j]
			numa[j]=numa[j-1]
			numa[j-1]=a
print(' '.join(list(map(str,numa))))
print('Stable')

#select
for i in range(0,n):
	minj=i
	b=0
	for j in range(i,n):
		if numb[j][1:]<numb[minj][1:]:
			minj=j
	b=numb[minj]
	numb[minj]=numb[i]
	numb[i]=b
print(' '.join(list(map(str,numb))))
if numb==numa:
	print('Stable')
else:
	print('Not stable')
		

