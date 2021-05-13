N,Ma,Mb=[int(x) for x in input().split()]
A=[]
B=[]
C=[]
for i in range(N):
	a,b,c=[int(x) for x in input().split()]
	A.append(a)
	B.append(b)
	C.append(c)


ANS=[[[-1 for k in range(401)] for j in range(401)] for i in range(41)]

INF=1000000000000000000000

def f(ind,wa,wb):
	global Ma
	global Mb
	global N
	if ANS[ind][wa][wb]==-1:
		if ind==0:
			if (wa+A[0])*Mb==(wb+B[0])*Ma:
				ANS[ind][wa][wb] = C[0]
			elif wa*Mb==wb*Ma and (wa!=0 and wb!=0):
				ANS[ind][wa][wb] = 0
			else:
				ANS[ind][wa][wb] = INF
		else:
			ANS[ind][wa][wb] = min(f(ind-1,wa,wb),f(ind-1,wa+A[ind],wb+B[ind])+C[ind])
	return ANS[ind][wa][wb]

ans=f(N-1,0,0)

if ans==INF:
	print(-1)
else:
	print(ans)