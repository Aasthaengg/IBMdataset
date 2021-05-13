a = int(input())
b = int(input())
r = ''
if a == b:
	r = 'EQUAL'
else:
	r = 'GREATER' if a > b else 'LESS'
print(r)