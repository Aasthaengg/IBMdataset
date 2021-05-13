N=int(input())






out=[]
if(N%2==0):
	for i in range(1,N+1):
		for j in range(i+1,N+1):
			if(i+j!=N+1):
				out.append(str(i)+" "+str(j))			
else:
	for i in range(1,N+1):
		for j in range(i+1,N+1):
			if(i+j!=N):	
				out.append(str(i)+" "+str(j))			

print(len(out))
for i in out:
	print(i)




