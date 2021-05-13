cards=[[i,j] for i in ['S','H','C','D'] for j in map(str,xrange(1,14))]
for i in xrange(int(raw_input())):
	cards.remove(raw_input().split())
for i in cards:
	print i[0],i[1]