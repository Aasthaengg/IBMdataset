N=int(input())
A=int(input())

if N-(N//500)*500<=A:
	print("Yes")
else:
	print("No")
