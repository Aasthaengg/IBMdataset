grp = ["S", "H", "C", "D"]
cards = []
for g in grp:
	for i in xrange(1, 13+1):
		cards.append("{0} {1}".format(g, i))
n = int(raw_input())
for i in xrange(n):
	card = raw_input()
	cards.remove(card)
for card in cards:
	print card