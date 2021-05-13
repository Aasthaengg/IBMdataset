def main():
	N,Y = map(int,input().split())
	for a in range(N+1):
		for b in range(N+1-a):
			y = 10000*a+5000*b+1000*(N-a-b)
			if y == Y :
				print(a,b,N-a-b)
				exit()
	print(-1,-1,-1)

if __name__ == '__main__':
	main()