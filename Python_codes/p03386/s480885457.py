A,B,K = map(int,input().split())
S = []
#list(range(A,B+1))
for i in range(K):
	S.append(A+i)
	S.append(B-i)

S = sorted(list(set(S)))

for i in range(len(S)):
	if A<=S[i]<=B:
		print(S[i])