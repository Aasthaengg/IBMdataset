n = int(input())
a = list(map(int, input().split()))

# 偶数番目(0-origin)を正とする場合
minA = 0
sumA = 0
for i in range(n):
	sumA += a[i]
	if i % 2 == 0:
		if sumA <= 0:
			minA += abs(sumA) + 1
			sumA += abs(sumA) + 1
	else:
		if sumA >= 0:
			minA += abs(sumA) + 1
			sumA -= abs(sumA) + 1

# 奇数番目(0-origin)を正とする場合
minB = 0
sumB = 0
for i in range(n):
	sumB += a[i]
	if i % 2 != 0:
		if sumB <= 0:
			minB += abs(sumB) + 1
			sumB += abs(sumB) + 1
	else:
		if sumB >= 0:
			minB += abs(sumB) + 1
			sumB -= abs(sumB) + 1

print(min(minA, minB))