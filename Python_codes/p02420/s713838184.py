while True:
	card=raw_input()
	if card=="-":
		break
	
	ct=int(raw_input())
	for i in range(ct):
		s=int(input())
		card=card[s:]+card[:s]
	print card