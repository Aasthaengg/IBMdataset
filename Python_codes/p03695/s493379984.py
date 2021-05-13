# C - Colorful Leaderboard
N = int(input())
a = list(map(int, input().split()))

lst = [0,0,0,0,0,0,0,0,0]

for i in range(N):
	for j in range(1,9):
		if a[i] < 400*j:
			lst[j-1] = 1
			break
	else:
		lst[8] += 1

if sum(lst[0:8]) == 0:
    min = 1
else:
    min = sum(lst[0:8])
max = sum(lst)

print(min,max)
