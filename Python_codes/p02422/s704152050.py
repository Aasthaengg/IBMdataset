str1 = list(input())
q = int(input())

for i in range(q):
	order = [str(x) for x in input().split()]
	if order[0] == 'replace':
		str1[int(order[1]):int(order[2])+1] = list(order[3]) 
		#print(str1)
	elif order[0] == 'reverse':
		str2 = str1[int(order[1]):int(order[2])+1]
		str1[int(order[1]):int(order[2])+1] = reversed(str2)
			
	else: #print
		print(*str1[int(order[1]):int(order[2])+1], sep='')