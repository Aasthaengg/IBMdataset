N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for i in range(M)]
answer = [1]*N

for i in range(M):
	if H[AB[i][0]-1] > H[AB[i][1]-1]:
		answer[AB[i][1]-1] = 0
	elif H[AB[i][0]-1] == H[AB[i][1]-1]:
		answer[AB[i][1]-1] = 0
		answer[AB[i][0]-1] = 0
	else:
		answer[AB[i][0]-1] = 0

print(sum(answer))