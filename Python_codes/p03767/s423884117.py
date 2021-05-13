def main():
	N = int(input())
	a = list(map(int, input().split()))

	a.sort()

	print(sum(a[N: 3 * N: 2]))


  
if __name__ == "__main__":
  	main()