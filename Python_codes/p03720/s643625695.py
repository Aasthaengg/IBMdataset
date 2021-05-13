def main():
	N, M = map(int, input().split())
	lst = [0] * N

	for _ in range(M):
		a, b = map(int, input().split())
		lst[a - 1] += 1
		lst[b - 1] += 1

	for i in range(N):
		print(lst[i])

  
if __name__ == "__main__":
  	main()