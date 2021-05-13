n = input()
taro_score = 0
hanako_score = 0
for i in range(n):
	taro,hanako = raw_input().split()
	if taro > hanako :
		taro_score += 3
	elif taro == hanako :
		taro_score += 1
		hanako_score += 1
	else :
		hanako_score += 3
print '%d %d' %(taro_score,hanako_score)