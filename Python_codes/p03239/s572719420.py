if __name__ == '__main__':

	n,t = map(int,input().split())
	
	cost = 1001
	for i in range(n):
		cn,tn = map(int,input().split())
		if tn <= t :
			cost = min(cost,cn)

	if cost == 1001:
		print("TLE")
	else:
		print(cost)
