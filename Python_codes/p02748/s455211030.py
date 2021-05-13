a,b,m = map(int,input().split())
price_a = list(map(int,input().split()))
price_b = list(map(int,input().split()))

minPrice = min(price_a) + min(price_b)

for i in range(m):
	x,y,c = map(int,input().split())
	price = price_a[x-1] + price_b[y-1] -c
	if price < minPrice:
		minPrice = price

print(minPrice)