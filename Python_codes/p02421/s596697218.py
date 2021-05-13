battle_number = int(raw_input())
Taro_score = 0
Hanako_score = 0

for x in xrange(battle_number):
	tcard, hcard = raw_input().split()

	if tcard > hcard:
		Taro_score += 3
	elif hcard > tcard:
		Hanako_score += 3
	elif tcard == hcard:
		Taro_score += 1
		Hanako_score += 1

print "%d %d" %(Taro_score, Hanako_score)