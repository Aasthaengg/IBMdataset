N=int(input())
A=input()
B=input()
C=input()
S=""
count=0
for i in range(N):
	S=[A[i],B[i],C[i]]
	if len(set(S))==3:
		count+=2
	elif len(set(S))==2:
		count+=1
print(count)