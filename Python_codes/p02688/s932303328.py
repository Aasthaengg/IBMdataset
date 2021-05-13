N, K = map(int, input().split())
d = [0] * K
A = [] 
for i in range(K):
	d[i] = int(input())
	A += list(map(int, input().split()))
answer = N -len(list(set(A)))

print(answer)