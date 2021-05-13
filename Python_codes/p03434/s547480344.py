def main():
	N = int(input())
	a = list(map(int, input().split()))
	len_a = len(a)

	a.sort(reverse = True)

	Alice = sum(a[0 : len_a : 2])
	Bob = sum(a[1 : len_a : 2])

	print(Alice - Bob)

  
if __name__ == "__main__":
  	main()