N=int(input())
tmp=0
M=0
for i in range (N):
	A,B=map(int,input().split())
	if tmp<A:
		tmp=A
		M=B
		
print(tmp+M)