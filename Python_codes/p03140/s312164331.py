N = int(input())
A = list(input())
B = list(input())
C = list(input())

count = 0 

for i in range(N):
	if A[i] == B[i] and A[i] == C[i]:
		continue
	elif A[i] == B[i] or A[i] == C[i] or B[i] == C[i]:
		count +=1
	else:
		count +=2
print(count)