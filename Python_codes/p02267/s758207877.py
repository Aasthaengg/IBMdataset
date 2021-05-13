n=int(input())
S=input().split()
q=int(input())
T=input().split()
cnt=0
for i in range(len(T)):
	
	flag=0
	
	for j in range(len(S)):
		
		if T[i]==S[j]:flag=1
		
	if flag==1:cnt+=1;
	
print(cnt)
