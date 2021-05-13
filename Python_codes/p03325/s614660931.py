n,r = int(raw_input()), 0
ais = map(int ,raw_input().split())
for ai in ais:
	while(ai % 2 == 0 ):
		ai /= 2
		r += 1
print r