n = int(input())
s = list(input())

red = s.count('R')

blue = s.count('B')

if(red>blue):
	print("Yes")

else:
	print("No")