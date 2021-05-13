n=int(input())
data={
	'S':[int(x) for x in range(1,14)],
	'H':[int(x) for x in range(1,14)],
	'C':[int(x) for x in range(1,14)],
	'D':[int(x) for x in range(1,14)]
	}
	

for i in range(0,n):
	s,r=input().split()
	r=int(r)
	data[s].remove(r)

for i in('S','H','C','D'):
	for v in data[i]:
		print(i,v)