a = input()
b = input()
month_a = int(a.split(" ")[0])
month_b = int(b.split(" ")[0])
if month_a != month_b:
	val = 1
else:
	val = 0
print(val)