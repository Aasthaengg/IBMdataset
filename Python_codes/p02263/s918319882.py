
list=input().split()

i=0

for j in range(len(list)):
	if list[i]=='+':
		list[i]=int(list[i-1])+int(list[i-2])
		del list[i-2]
		del list[i-2]
		i-=2
	elif list[i]=='-':
		list[i]=int(list[i-2])-int(list[i-1])
		del list[i-2]
		del list[i-2]
		i-=2
	elif list[i]=='*':
		list[i]=int(list[i-1])*int(list[i-2])
		del list[i-2]
		del list[i-2]
		i-=2
	elif list[i]=='/':
		list[i]=int(list[i-2])/float(list[i-1])
		del list[i-2]
		del list[i-2]
		i-=2
	i+=1

print(list[0])
