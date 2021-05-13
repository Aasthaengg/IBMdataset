from itertools import product

x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB = []
for (a, b) in product(A, B):
	AB.append(a + b)

AB.sort(reverse=True)

res = []
for (ab, c) in product(AB[:min(3000, x*y*z)], C):
	res.append(ab + c)

res.sort(reverse=True)

for i in range(k):
	print(res[i])