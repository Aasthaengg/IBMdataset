n = input()
cur = 0
for x in n:
	cur += int(x)
if cur % 9 == 0:
	print("Yes")
else:
	print("No")