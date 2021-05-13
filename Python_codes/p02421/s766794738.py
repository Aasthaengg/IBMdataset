num = int(raw_input())

taro = 0
hanako = 0

for i in range(num):
	cards = raw_input().split()
	if cards[0] < cards[1]:
		hanako += 3
	elif cards[0] == cards[1]:
		taro += 1
		hanako += 1
	else:
		taro += 3

print("{:} {:}".format(taro, hanako))