def main():
	N = int(input())
	T, A = map(int, input().split())
	H = list(map(int, input().split()))

	lst = [1000] * N

	for i in range(N):
		lst[i] = abs(T - H[i] * 0.006 - A)

	print(lst.index(min(lst)) + 1)


  
if __name__ == "__main__":
  	main()