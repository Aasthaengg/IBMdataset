N = int(input())
A = list(map(int,input().split()))

tmp = 1
for aa in A:
	if aa%2 == 0:
		tmp *= 2
	else:
		tmp *= 1

#if len(A) == 1:

print(3**N-tmp)