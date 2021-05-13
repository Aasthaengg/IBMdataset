L=list(map(int,input().split()))
A=60*L[0]+L[1]
B=60*L[2]+L[3]
if B-A <= L[4]:
	print("0")
else:
	print(str(B-A-L[4]))