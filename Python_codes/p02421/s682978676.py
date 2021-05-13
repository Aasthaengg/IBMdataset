n = int(input())

t = 0
h = 0
for i in range(n):
	card1, card2 = map(str, input().split())
	if card1 > card2:
		t += 3
	elif card1 < card2:
		h += 3
	else:
		t += 1
		h += 1

print(str(t) + ' ' + str(h))

