
A,B,K=input().split()
A=int(A)
B=int(B)
K=int(K)
turn=0
while(1):
	if(turn==K):
		break
	if(turn%2==0):#高橋くん
		if(A%2==1):
			A-=1
		B+=A//2
		A-=A//2
	else:#青木くん
		if(B%2==1):
			B-=1
			
		A+=B//2
		B-=B//2
	turn+=1
print(str(A)+" "+str(B))