[n,t]=list(map(int,input().split()))
alist=list(map(int,input().split()))
salist=[alist[1]-alist[0]]
saisho=min(alist[0],alist[1])
for i in range(1,n-1):
	saisho=min(saisho,alist[i])
	salist.append(alist[i+1]-saisho)
saidai=max(salist)
kaisu=salist.count(saidai)
print(kaisu)