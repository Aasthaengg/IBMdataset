A,B,C = map(int,input().split())

if A == B:
	answer = C
elif B == C:
	answer = A
else:
	answer = B

print(answer)