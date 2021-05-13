W = raw_input().lower()
c = 0
while True:
	T = raw_input()
	if T == 'END_OF_TEXT':
		break
	t = T.split(" ")
	for i in t:
		if i.lower() == W.lower():
			c += 1
print c