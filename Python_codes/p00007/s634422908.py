price = 100000
n = input()
for i in range(n):
	price = price * 105 / 100
	if price % 1000 != 0:
		price -= (price % 1000)
		price += 1000
print price