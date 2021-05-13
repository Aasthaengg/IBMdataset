def main():
	num = 0

	_ = input()
	s_set = set(map(int, input().split()))

	_ = input()
	t_set = set(map(int, input().split()))
	for t in t_set:
		if t in s_set:
			num +=1
	
	print(num)

if __name__ == '__main__':
	main()