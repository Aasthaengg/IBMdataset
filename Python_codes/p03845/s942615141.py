N = int(input())
T = list(map(int,input().split()))
M = int(input())
P = [list(map(int,input().split())) for i in range(M)]

def calc(lis):
	T2 = T.copy()
	T2[lis[0]-1] = lis[1]
	return sum(T2)

for i in range(M):
	print(calc(P[i]))