import sys

message = str(input())

for c in message:
	order = ord(c)
	if order >= 65 and order <= 90:
		sys.stdout.write(chr(order + 32))
	elif order >= 97 and order <= 122:
		sys.stdout.write(chr(order - 32))
	else:
		sys.stdout.write(c)
print()
