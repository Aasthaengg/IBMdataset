N, H, W = list(map(int, input().strip().split(' ')))

AB = []

cnt = 0

for i in range(N):
	AB.append(list(map(int, input().strip().split(' '))))	#[A][B]
	
	
for i in range(N):
	if int(AB[i][0]) >= H:
			if int(AB[i][1]) >= W:
				cnt += 1

print(cnt)