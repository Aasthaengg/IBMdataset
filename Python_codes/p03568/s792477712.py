n = int(input())
A = list(map(int, input().split()))

cnt_even, cnt_odd = 0, 0
for i in range(n):
	if A[i] % 2 == 0:
		cnt_even += 1
	else:
		cnt_odd += 1

cnt = 3 ** n - (2 ** (cnt_even))
print(cnt)