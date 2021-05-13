findmoji = input()

mojilist = []
cnt = 0
while True:
	oneline = input()
	if oneline == "END_OF_TEXT":
		break
	else:
		s = oneline.split(" ")
		for m in s:
			if m.lower() == findmoji:
				cnt += 1

print(cnt)

