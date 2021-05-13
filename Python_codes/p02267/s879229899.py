
n=int(input())
S=[]
S=input().split()
q=int(input())
T=[]
T=input().split()
point=0
for i in range(q):	
	for j in range(n):
		if T[i]==S[j]:
			point+=1
			break
			
print(point)
