
def main():
	n, m =  map(int , input().split())
	ab = []
	for i in range(0 , n):
		ab.append(list(map(int , input().split())))
	ab.sort()
	ans = 0
	for i in range(0 , n):
		if (m-ab[i][1]>=0):
			m = m-ab[i][1]
			ans = ans+(ab[i][0]*ab[i][1])
		elif(m>0):
			ans = ans+(m*ab[i][0])
			m  = 0
	print(ans)
if __name__ =="__main__":
	main()