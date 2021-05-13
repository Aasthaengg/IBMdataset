import math
def main():
	n , m = map(int,input().split())
	m += m+1
	print(math.ceil(n/m))


main()
