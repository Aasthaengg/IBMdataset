#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

N,M=input2()
L,R=[],[]
for i in range(M):
	l,r=input2()
	L.append(l)
	R.append(r)

MIN=0
MAX=N

for j in range(M):
	if L[j]>MIN:
		MIN=L[j]
	if R[j]<MAX:
		MAX=R[j]

if MAX<MIN:
	print(0)
else:
	print((MAX-MIN)+1)
