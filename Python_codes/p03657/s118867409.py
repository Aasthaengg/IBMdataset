import sys
a, b = map(int, input().split())
if a != 0 and a%3 == 0:
	print("Possible")
	sys.exit()
if b != 0 and b%3 == 0:
	print("Possible")
	sys.exit()
if a != 0 and b != 0 and (a+b)%3 == 0:
	print("Possible")
	sys.exit()

print("Impossible")