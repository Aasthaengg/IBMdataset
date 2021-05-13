def n_nimotsu_if_P(P, k, arr):
	weight = 0
	n_trucks = 1
	for i, a in enumerate(arr):
		if P < a:
			return i
		if weight + a <= P:
			weight += a
		else:
			n_trucks += 1
			weight = a
		if n_trucks == k + 1:
			return i

	return len(arr)

n, k = map(int, input().split())
luggages = []
for _ in range(n):
	luggages.append(int(input()))

left, right = 0, 10000 * n
i_break = 0
while right - left > 1:
	mid = (left + right) // 2
	if n <= n_nimotsu_if_P(mid, k, luggages):
		right = mid
	else:
		left = mid

print(right)
