N, M, X = map(int, input().split())

l = []
for i in range(N):
	a = list(map(int, input().split()))
	l.append(a)

money_min = 100000000
for bit in range(1 << N):
	bag = []
	for i in range(N):
		if ((bit >> i) & 1):
			bag.append(l[i])
	skill = [0]*M
	enough = [0]*M
	money = 0
	for sub in bag:
		money += sub[0]
		#print(money)
		for j in range(M):
			skill[j] += sub[j+1]
		#print(skill)
	for k in range(M):
		if skill[k] >= X:
			enough[k] += 1
		else:
			enough[k] = enough[k]
	if 0 not in enough:
		if money < money_min:
			money_min = money
		else:
			money_min = money_min

if money_min != 100000000:
	print(money_min)
else:
	print(-1)