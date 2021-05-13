tmp = input()
tmp = tmp.split(" ")
x,y = map(int,tmp)
if x == y:
	print("a == b")

elif x > y:
	print("a > b")

else:
	print("a < b")