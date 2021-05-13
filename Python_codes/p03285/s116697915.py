from sys import exit

n=int(input())

while n>0:
	if n%7==0:
		print("Yes")
		exit()
	n-=4
	if n==0:
		print("Yes")
		exit()

print("No")