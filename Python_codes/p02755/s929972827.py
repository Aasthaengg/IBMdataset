import math
if __name__ == '__main__':
	a,b = map(int,input().split())

	flg = False
	for x in range(1,1001):
		tmp1 = math.floor(x * 0.08)
		tmp2 = math.floor(x * 0.1)
		if tmp1 == a and tmp2 == b:
			print(x)
			flg = True
			break
	if flg == False:
		print("-1")