n=int(input())
L=list(map(int, input().split()))

M=sorted(L)
a=M[n//2]
b=M[n//2-1]

for i in range(n):
	if L[i]>=a:
		print(b)
	else:
		print(a)