s = list(input())
c = 0
for i in range(97,97 + 26):
	if chr(i) not in  s:
		print(chr(i))
		break
	c += 1
if c == 26:
  print('None')