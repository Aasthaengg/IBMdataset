def shuffle(l,h):
	l.extend(l[0:h])
	del l[0:h]
	
while True :
	card_list = list(raw_input())
	if card_list == ['-']:
		break
	else :
		m = input()
		h_count = [0]*m
		for i in range(m):
			h_count[i] = input()
			shuffle(card_list,h_count[i])
		print("".join(card_list))