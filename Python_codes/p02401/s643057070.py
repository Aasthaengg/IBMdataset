import sys
line = sys.stdin.readline()
num = []
while line:
	a,op,b = line.split()
	if op == "+":
		num.append(int(a)+int(b))
	elif op == "-":
		num.append(int(a)-int(b))
	elif op == "*":
		num.append(int(a)*int(b))
	elif op == "/":
		num.append(int(a)/int(b))
	else:
		break
	line = sys.stdin.readline()
for i in num:
	print str(i)