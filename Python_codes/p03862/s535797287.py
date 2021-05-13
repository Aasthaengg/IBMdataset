

n, x = map(int, raw_input().split())
ais = map(int, raw_input().split())


q= sum([ai - min(x,ai) for ai in ais])

ais = [min(x,ai) for ai in ais]

for ii in range(1,len(ais)):
	if ais[ii] + ais[ii-1] > x:
		q += ais[ii] + ais[ii-1] - x
		ais[ii] -= ais[ii] + ais[ii-1] - x
print q