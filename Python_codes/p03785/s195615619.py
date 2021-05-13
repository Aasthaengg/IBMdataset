def main():
	N, C, K = map(int, input().split())
	
	T = [int(input()) for _ in range(N)]
	T = sorted(T)

	num_bus = 1
	num_passenger = 1
	first_passenger = T[0]

	for i in range(1, N):
		if first_passenger + K < T[i]:
			first_passenger = T[i]
			num_passenger = 1
			num_bus += 1
		elif num_passenger == C:
			first_passenger = T[i]
			num_passenger = 1
			num_bus += 1
		else:
			num_passenger += 1

	print(num_bus)
		

 
if __name__ == "__main__":
  	main()