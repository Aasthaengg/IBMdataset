def main():
	n = int(input())
	dictionary = {}

	for _ in range(n):
		order, code = input().split()
		if order == 'insert':
			dictionary[code] = 1
		elif order == 'find':
			if code in dictionary:
				print('yes')
			else:
				print('no')
		else:
			raise Exception('InputError')

if __name__ == '__main__':
	main()