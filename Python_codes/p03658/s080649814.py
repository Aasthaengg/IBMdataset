def main():
	N, K = map(int, input().split())
	l = list(map(int, input().split()))

	l.sort(reverse = True)

	print(sum(l[0: K]))

  
if __name__ == "__main__":
  	main()