while True:
	cards = input()
	if cards == '-':
		break
	n = int(input())
	
	for _ in range(n):
		shuffle = int(input())
		cards = cards[shuffle:] + cards[:shuffle]
		
	print(cards)