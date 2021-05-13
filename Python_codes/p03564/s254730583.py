N = int(input())
K = int(input())

score = 1
for i in range(N):
	if score*2 > score+K:
		score += K
	else: score *= 2
print(score)