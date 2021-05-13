n = int(raw_input())
lst = []
#store all the cards
for i in ["S","H","C","D"]:
	for j in xrange(1,14):
		lst.append("{0} {1}".format(i,j))
#discard the given cards
for i in range(n):
	a = raw_input()
	lst.remove(a)
#print the result
for i in range(len(lst)):
	print lst[i]