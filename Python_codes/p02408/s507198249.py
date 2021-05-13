card = {
	'S':[1,2,3,4,5,6,7,8,9,10,11,12,13],
	'H':[1,2,3,4,5,6,7,8,9,10,11,12,13],
	'C':[1,2,3,4,5,6,7,8,9,10,11,12,13],
	'D':[1,2,3,4,5,6,7,8,9,10,11,12,13],
	}
dr = ['S','H','C','D']

n = int(raw_input())

for i in xrange(n):
	fffff,ddddd = map(str,raw_input().split())
	card[fffff].remove(int(ddddd))
	
for var in card:
	card[var].sort()
	
for var in dr:
	for i in xrange(len(card[var])):
		print var,card[var][i]