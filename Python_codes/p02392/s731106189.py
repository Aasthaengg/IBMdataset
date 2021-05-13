deglist = raw_input().split(" ")
a = int(deglist[0])
b = int(deglist[1])
c = int(deglist[2])
if a < b and b < c:
	print("Yes")
else:
	print("No")