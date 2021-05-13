chars = ""
while True:
	try:
		chars += raw_input()
	except EOFError:
		break

#chars = raw_input()
low_chars = chars.lower()
#print low_chars

alphabet = "abcdefghijklmnopqrstuvwxyz"

for c in alphabet:
	cnt = low_chars.count(c)
	print("{:} : {:}".format(c, cnt))