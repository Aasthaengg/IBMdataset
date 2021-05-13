import collections
def f(n,ais):
	cc,extra = collections.Counter(),0
	for ai in ais:
		if ai/400 < 8: cc[ai/400] +=1
		else: extra +=1
	print len(cc) + (1 if (len(cc) == 0 and extra) else 0), min(10000, len(cc) + extra)
	#print min(cc.values() or [0]), max(cc.values() or [0]) + extra
f(int(raw_input()), map(int, raw_input().split()))