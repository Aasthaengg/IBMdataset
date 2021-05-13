l = list(map(int,input().split()))
a = l[0]
b = l[1]
x = l[2]
if a%x == 0:
	print(b//x-a//x +1)
else:
	print(b//x-a//x)