a,b,c = map(int,raw_input().split())
lst = []
for i in range(a,b+1):
	if c%i == 0:
		lst.append(i)
print len(lst)