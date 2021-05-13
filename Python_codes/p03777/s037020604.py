i_list = input().split()
a = i_list[0]
b = i_list[1]
r = ''
if a == 'H':
	r = b
else:
	r = 'H' if b == 'D' else 'D'
print(r)