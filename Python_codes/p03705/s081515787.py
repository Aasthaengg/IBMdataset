N, A, B = map(int, input().split())

if A == B :
	print(1)
	exit()

print(max(B*(N-1)+A-(A*(N-1)+B)+1,0))