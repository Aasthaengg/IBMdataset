import sys

n = input()
a_uni = [[[0 for i in range(10)]for i in range(3)]for i in range(4)]
for i in range(n):
	b,f,r,v = map(int,raw_input().split())
	a_uni[b-1][f-1][r-1] += v
for i in range(4):
	for j in range(3):
		for k in range(10):
			if k==9:
				sys.stdout.write(' ')
				print(a_uni[i][j][k])
			else :
				sys.stdout.write(' ')
				sys.stdout.write(str(a_uni[i][j][k]))
	if not i==3:
		print '####################'