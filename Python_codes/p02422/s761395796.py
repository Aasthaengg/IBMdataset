str = list(input())
num = int(input())

for num in range(num):
	ord = input().split()
	start = int(ord[1])
	end = int(ord[2]) + 1
	
	if ord[0] == 'replace':
		rep = list(ord[3])
		for i in range(start, end):
			str[i] = rep[i - start]
			
	elif ord[0] == 'reverse':
		temp = ''.join(str[start:end])
		rev = list(temp[::-1])
		
		for i in range(start, end):
			str[i] = rev[i - start]
	else:
		print(''.join(str[start:end]))