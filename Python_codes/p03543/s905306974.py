from sys import exit
n=input()
for i in range(10):
	if str(i)*3 in n:
		print("Yes")
		exit(0)
print("No")