from string import ascii_lowercase as asc
n = int(input())
card = []
point = [0,0]
for i in range(n):
	card.append(list(map(str,input().split())))
for k in range(len(card)):
	if card[k][0] == card[k][1]:
		point[0] += 1
		point[1] += 1
	elif card[k][0] == card[k][1][:len(card[k][0])]:
		point[1] += 3
	elif card[k][1] == card[k][0][:len(card[k][1])]:
		point[0] += 3
	else:
		s = 0
		while True:
			if card[k][0][s] == card[k][1][s]:
				s += 1
			else:
				break
		for kk in asc:
			if card[k][0][s] == kk:
				point[1] += 3
				break
			elif card[k][1][s] == kk:
				point[0] += 3
				break
print(" ".join(list(map(str,point))))
