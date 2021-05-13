A,B,C,D=map(int,input().split())
E=abs(A-B)
F=abs(B-C)
G=abs(A-C)
if G<=D or (E<=D and F<=D):
	print("Yes")
else:
	print("No")