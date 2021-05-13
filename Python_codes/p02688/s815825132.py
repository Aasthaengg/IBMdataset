N, K = map(int, input().split())

answer = [1] * N

for i in range(K):
	d = int(input())
	tmp = map(int, input().split())

	for j in tmp:
		answer[j-1] = 0

print(sum(answer))