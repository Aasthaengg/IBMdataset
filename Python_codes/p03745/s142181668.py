def main():
	N = int(input())
	A = list(map(int, input().split()))

	is_increasing = True
	is_first = True
	ans = 1

	for i in range(1, N):
		if is_first == True:
			if A[i - 1] < A[i]:
				is_increasing = True
				is_first = False
			elif A[i - 1] > A[i]:
				is_increasing = False
				is_first = False
		else:
			if is_increasing == True and A[i - 1] > A[i]:
				ans += 1
				is_first = True
			elif is_increasing == False and A[i - 1] < A[i]:
				ans += 1
				is_first = True

	print(ans)



 
if __name__ == "__main__":
  	main()