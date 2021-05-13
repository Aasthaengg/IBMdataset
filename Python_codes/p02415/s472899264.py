import sys
A=input().split()
for i in A:
	sys.stdout.write(i.swapcase())
	if i!=A[-1]:
		sys.stdout.write(" ")
print()