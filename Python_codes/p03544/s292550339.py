#A,B,C=map(float,input().split())
#a,b,c=map(int,input().split())
N=int(input())
Lm=2
Ln=1
Lo=2
if N==0:
	print(2)
elif N==1:
	print(1)
else:
	for i in range(N-1):
		Lo=Lm+Ln
		Lm=Ln
		Ln=Lo
	print(Lo)
