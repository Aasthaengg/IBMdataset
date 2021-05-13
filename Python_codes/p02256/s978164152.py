import sys

input_list = map(int, raw_input().split())

x = input_list[0]
y = input_list[1]

if x < y:
	tmp = x
	x = y
	y = tmp
elif x == y:
	print(x)
	sys.exit(0)


r = 0
while y != 0:
	r = x % y
	x = y
	y = r

print(x)
	

