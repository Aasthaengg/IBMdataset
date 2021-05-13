x, y = map(int, input().split())
ans = False
 
for i in range(101):
	for j in range(101):
		if i+j == x and 2*i+4*j == y:
			ans = True
if ans:
	print("Yes")
else:
	print("No")