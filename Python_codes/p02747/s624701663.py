
s = input()

if len(s) % 2 ==1:
	print('No')
	exit()

if s == "hi"* (len(s) // 2):
	print('Yes')
else:
	print('No')