
A = [None, None, None]
B = [0, None, None]
C = [None, None, None]

for i in range(3):
	 A[i] = list(map(int,input().split())) 

flag = True

for i in range(3):
	for j in range(3):
		
		if B[i] == None:
			B[i] = A[i][j] - C[j]
		elif C[j] == None:
			C[j] = A[i][j] - B[i]
		elif A[i][j] != B[i] + C[j]:
			flag = False
		
if flag == True :
	print ("Yes")
else :
	print ("No")