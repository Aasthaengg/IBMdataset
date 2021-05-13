stack = []
a=1
while not a==0:
	a=input()
	stack.append(a)
stack.remove(0)
for i, a in enumerate(stack):
	print "Case %s: %s" % (i+1,a)