
while(1):
	
	a, op, b = map(str, input().split())
	if op == "+":
		print("%d" % (int(a)+int(b)))
	elif op == "-":
		print("%d" % (int(a)-int(b)))
	elif op == "/":
		print("%d" % (int(a)//int(b)))
	elif op == "*":
		print("%d" % (int(a)*int(b)))
	else:
		break