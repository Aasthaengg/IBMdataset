input()
A = list(map(int, input().split()))
B = set()
for a in A:
	B.add(a)
if len(A) == len(B):
	print('YES')
else:
	print('NO')