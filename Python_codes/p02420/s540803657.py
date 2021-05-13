deck,shuf = [],[]
while True:
	dec = str(input())
	if dec == "-":
		break
	deck.append(dec)
	m =int(input())
	h = []
	for i in range(m):
		h.append(int(input()))
	shuf.append(h.copy())
for k in range(len(deck)):
	for kk in range(len(shuf[k])):
		deck[k] = deck[k][shuf[k][kk]:] + deck[k][:shuf[k][kk]]
	print(deck[k])
