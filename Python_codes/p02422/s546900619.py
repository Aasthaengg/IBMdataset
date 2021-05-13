string=list(input())
num=int(input())
orders=[]
for n in range(num):
	orders.append(input().split(' '))

for order in orders:
	if order[0] == 'print':
		a=int(order[1])
		b=int(order[2])
		target_l=string[a:b+1]
		for i in target_l:
			print(i,end="")
		print()
		
	elif order[0] == 'reverse':
		a=int(order[1])
		b=int(order[2])
		target_l=string[a:b+1]
		for i in range(len(target_l)//2):
			tmp=target_l[i]
			target_l[i]=target_l[-(i+1)]
			target_l[-(i+1)]=tmp

		new_l=string[:a]+target_l+string[b+1:]
		string=new_l

	elif order[0] == 'replace':
		a=int(order[1])
		b=int(order[2])
		rep=list(order[3])
		for i,x in enumerate(string[a:b+1]):
			ii=i+a
			string[ii]=rep[i]





