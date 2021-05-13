import statistics
while True:
	if int(input()) == 0: break
	print('%.8f' % statistics.pstdev(list(map(int, input().split()))))
