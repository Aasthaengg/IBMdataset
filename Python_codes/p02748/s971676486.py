A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

minP = min(a) + min(b)

for i in range(M):
	x, y, c = map(int, input().split())
	x, y = x - 1, y - 1
	price_with_coupon = a[x] + b[y] - c
	minP = min(minP, price_with_coupon)

print(minP)