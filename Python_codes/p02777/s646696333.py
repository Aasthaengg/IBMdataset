S, T = input().rstrip().split()
A, B = [int(v) for v in input().rstrip().split()]
U =  input().rstrip()
if U == S:
	A -= 1
else:
	B -= 1

print('{} {}'.format(A, B))
