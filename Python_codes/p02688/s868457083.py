N, K = list(map(int, input().split()))
ans = [1 for _ in range(N)]
for i in range(K):
	d = int(input())
	a = list(map(int, input().split()))
	for j in a:  ans[j - 1] = 0
print(sum(ans))