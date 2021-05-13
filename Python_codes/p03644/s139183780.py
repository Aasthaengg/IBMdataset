def divide_by_2(num):
	cnt = 0		

	while True:
		if num % 2 != 0:
			break
		num /= 2
		cnt += 1
	
	return cnt



def main():
	N = int(input())

	max_cnt = -1
	ans = 0

	for num in range(1, N + 1):
		cnt = divide_by_2(num)

		if max_cnt < cnt:
			max_cnt = cnt
			ans = num

	print(ans)


  
if __name__ == "__main__":
  	main()