import math

if __name__ == '__main__':

	n,x = map(int,input().split())

	A = []
	for i in range(n):
		A.append(int(input()))

	cnt = 0
	sm = sum(A)
	x = x - sm
	cnt += len(A)
	
	if x != 0:
		mi = min(A)
		cnt += math.ceil(x // mi)

	print(cnt)