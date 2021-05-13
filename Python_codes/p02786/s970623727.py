def myfunc(N):
	if(N  <= 1):
		return 1
	return 2 * myfunc(int(N/2)) + 1

if __name__ == "__main__":
	N = int(input())
	print(myfunc(N))