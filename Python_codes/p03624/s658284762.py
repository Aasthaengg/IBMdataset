A="abcdefghijklmnopqrstuvwxyz"
S=input()
S=sorted(set(S))

for i in range(len(S)):
	if S[i]!=A[i]:
		print(A[i])
		exit()
if len(S)<len(A):
	print(A[len(S)])
	exit()
print("None")