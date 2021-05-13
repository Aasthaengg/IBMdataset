ais = map(int, raw_input().split())
if sum(ais[:2]) == sum(ais[2:]):
	print 'Balanced'
elif sum(ais[:2]) > sum(ais[2:]):
	print 'Left'
elif sum(ais[:2]) < sum(ais[2:]):
	print 'Right'
