def isPacked(numcar, maxweight, packs):
	weight = 0  # 一台当たりの積載量
	k = 1  # トラック台数

	for j in range(len(packs)):
		if packs[j] > maxweight:
			return False
		if weight + packs[j] > maxweight:
			k = k + 1
			weight = packs[j]
		else:
			weight = weight + packs[j]
		if k > numcar:
			return False

	return True


n, k = map(int, input().split())  # 5,3
W = []  # 8, 1, 7, 3, 9
PMAX = 0

for i in range(n):
	W.append(int(input()))
for i in W:
	PMAX = PMAX + i

#print(W)
#print(PMAX)

#print(isPacked(k, 5, W))
left = 0
right = PMAX + 1

while left < right:
	mid = (left + right) // 2
#	print('{0} {1} {2}'.format(left, mid, right))
	booleanPacked = isPacked(k, mid, W)
	if booleanPacked == True and isPacked(k, mid - 1, W) == False:
		print(mid)
		exit(0)
	elif booleanPacked == True:
		right = mid
	elif booleanPacked == False:
		left = mid + 1

