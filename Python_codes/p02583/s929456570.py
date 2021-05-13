n=int(input())
M=list(map(int,input().split()))
M.sort()
dic={}
dic[M[0]]=1
for i in range(1,n):
	if(M[i]!=M[i-1]):
		dic[M[i]]=1
	else:
		dic[M[i-1]]+=1

L=list(dic.keys())
l=len(L)
L.sort()
count=0
for i in range(0,l):
	for j in range(0,i):
		for k in range(0,j):
			if(L[i]<L[j]+L[k]):
				count+=dic[L[i]]*dic[L[j]]*dic[L[k]]
print(count)