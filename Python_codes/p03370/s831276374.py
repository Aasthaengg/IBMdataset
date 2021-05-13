def main():
	N, X = map(int, input().split())
	m = [0] * N

	for i in range(N):
		m[i] = int(input())

	X -= sum(m)

	cnt = N
	cnt += X // min(m)
	
	print(cnt)

  
if __name__ == "__main__":
  	main()