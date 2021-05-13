import sys 

inp=sys.stdin.readline()


def coffeeLike(inp):
	
	li=list(inp)
	if(len(li)>=6):
		if (li[2]==li[3]) and (li[4]==li[5]):
			print("Yes")
		else:
			print("No")
	else:
		print("No")
		
	
coffeeLike(inp)	