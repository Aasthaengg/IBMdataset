def main():
	N = int(input())
	d = [0] * N

	for i in range(N):
		d[i] = int(input())

	num = [0] * 101

	for i in range(N):
		num[d[i]] += 1

	ans = 0

	for i in range(101):
		if num[i] > 0:
			ans += 1

	print(ans)

  
if __name__ == "__main__":
  	main()