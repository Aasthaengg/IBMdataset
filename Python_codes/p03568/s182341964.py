N = int(input())
A = list(map(int, input().split()))

tot = 3 ** N

cnt_odd, cnt_even = 0,0

for i in range(N):
	if A[i] % 2 == 0:
		cnt_even += 1
	else:
		cnt_odd += 1

ans = tot - (2**cnt_even)*(1**cnt_odd)
print(ans)