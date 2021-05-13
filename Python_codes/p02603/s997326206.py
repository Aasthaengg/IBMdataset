N = int(input())
A = list(map(int, input().split()))

fm = 1000
nm = (0, 0)

for a in A:
	nfm = max(fm, nm[0] * a + nm[1])
	nnm = max(nm, (fm//a, fm - fm//a*a))

	fm, nm = nfm, nnm

print(fm)
