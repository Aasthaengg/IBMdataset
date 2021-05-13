s = 0
n = list(map(int, str(input())))
for i in range(len(n)):
	s+=n[i]
if(s%9==0):
	print("Yes")
else:
	print("No")