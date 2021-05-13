N = int(input())
A = list(map(int,input().split()))
p1, p2 = 0, 0
for i in range(N):
	max_A = max(A)
	if i % 2 == 0:
		p1 += max_A
	else:
		p2 += max_A
	A.remove(max_A)
print(p1 - p2)