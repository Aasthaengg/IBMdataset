a = list(input())
b = list(input())
c = list(input())
# print('a',a)
# print('b',b)
# print('c',c)
# exit()
ptr = 'a'
while (True):
	if ptr == 'a':
		if a == []:
			print('A')
			break
		ptr = a.pop(0)
	if ptr == 'b':
		if b == []:
			print('B')
			break
		ptr = b.pop(0)
	if ptr == 'c':
		if c == []:
			print('C')
			break
		ptr = c.pop(0)
