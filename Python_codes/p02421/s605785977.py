n = int(input())

taro_score = 0
hanako_score = 0
for i in range(n):
	words = input().split()
	taro_word = words[0]
	hanako_word = words[1]

	if taro_word == hanako_word:
		taro_score += 1
		hanako_score += 1
	elif taro_word > hanako_word:
		taro_score += 3
	else:
		hanako_score += 3

print("{0} {1}".format(taro_score, hanako_score))