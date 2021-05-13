N = int(input())
A = []
for i in range(1, 10):
	for j in range(1, 10):
		A.append(i * j)
ans = 'Yes' if N in A else 'No'
print(ans)