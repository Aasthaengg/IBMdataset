k=map(int,raw_input().split(" "))
vec=k[0]
col=k[1]

omatrix=[]
for i in range(vec+1):
	omatrix+=[[0]*(col+1)]

for i in range(vec):
	ipt=map(int,raw_input().split(" "))
	for j in range(col):
		omatrix[i][j]+=ipt[j]

for i in range(vec):
	omatrix[i][col]+=sum(omatrix[i])


for j in range(col+1):
	vsum=0
	for i in range(vec):
		vsum+=omatrix[i][j]
	omatrix[vec][j]+=vsum


for i in range(vec+1):
	for j in range(col+1):
		if j==col:
			print omatrix[i][j]
		else:
			print omatrix[i][j],