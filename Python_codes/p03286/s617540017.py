n = int(input())
ansl = []
if n == 0:
	print(0)
	exit()
while n != 0:
	if n % 2 == 1:
		ansl.append("1")
		n -= 1
	else:
		ansl.append("0")
	n //= -2
print("".join(ansl)[::-1])