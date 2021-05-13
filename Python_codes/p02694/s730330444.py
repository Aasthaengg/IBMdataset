# abc165_b
x, money, year = int(input()), 100, 0
while x > money:
	money += money // 100
	year += 1
print(year)