n = int(input())
p_taro = 0
p_hanako = 0
for i in range(n):
	taro, hanako = map(str, input().split())
	cards = tuple(sorted((taro, hanako)))
	#print(cards)

	if taro == hanako:
		p_taro += 1
		p_hanako += 1
	else:
		if cards == (taro, hanako):
			p_hanako += 3
			#print("hanako win")
		else:
			p_taro += 3
			#print("taro win")

print(p_taro, p_hanako)