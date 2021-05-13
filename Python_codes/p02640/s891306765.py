if __name__ == '__main__':

	x,y = map(int,input().split())
	
	flg = False

	for i in range(0,x+1):
		for j in range(0,y+1):
			if i + j == x and 2*i + 4*j == y:
				flg = True
				break

	if flg:
		print("Yes")
	else:
		print("No")
