w ,h ,x ,y ,r = input().split(' ')
if int(x) <= int(w) - int(r) and int(x) >= int(r) and int(y) <= int(h) - int(r) and int(y) >= int(r):
	print("Yes")
else:
	print("No")