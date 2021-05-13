n = int(input())
best = 0
for i in range(2, n+1, 2):
	c = 0
	j = i
	while(j % 2 == 0):
		j = j // 2
		c += 1
	best = max(best, c)
print(2 ** best)