def smaller(x, y):
	if x < y:
		return x
	return y

N, A, B = map(int, input().split())
print(smaller(N*A, B))