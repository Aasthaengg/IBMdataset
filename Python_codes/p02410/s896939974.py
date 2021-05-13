array_data = map(int, raw_input().split())
n = array_data[0]
m = array_data[1]

A = []
for i in range(n):
	partial_A = map(int, raw_input().split())
	A.append(partial_A)

b = []
for i in range(m):
	partial_b = int(raw_input())
	b.append(partial_b)

ans = []
for i in range(n):
	partial_ans = 0
	for j in range(m):
		partial_ans += A[i][j] * b[j]
	ans.append(partial_ans)

for i in range(len(ans)):
	print ans[i]