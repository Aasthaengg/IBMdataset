while True:
	w=input()
	if w=='-':
		break
	else:
		list=[]
		for i in w:
			list.append(i)
		num=int(input())
		for i in range(num):
			s=int(input())
			for i in range(s):
				list.append(list.pop(0))
	print(''.join(list))
		
