A,B,C,D = map(int,input().split())

if (A * B) >(C * D):
	answer = A * B
elif (C * D) > (A * B):
	answer = C * D
elif (A * B) == (C * D):
	answer = C * D
print(answer)