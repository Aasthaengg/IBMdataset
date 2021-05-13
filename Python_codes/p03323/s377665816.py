def LI():
	return [ int(s) for s in input().split() ]
  
a,b = LI()
 
print('Yay!') if a <= 8 and b <= 8 else print(':(')