N,A,B = map(int,input().split())

if N * A <= B:
	answer = N * A
else:
	answer = B

print(answer)