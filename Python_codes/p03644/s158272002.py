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

	lst = [-1] * (N + 1)

	for num in range(1, N + 1):
		cnt = divide_by_2(num)
		lst[num] = cnt

	print(lst.index(max(lst)))


  
if __name__ == "__main__":
  	main()